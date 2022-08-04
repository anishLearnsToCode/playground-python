# -*- coding: utf-8 -*-
import logging.config
import configparser
import sys

# pdf libraries
from collections import OrderedDict
from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject, NumberObject

# Database access
import cx_Oracle

# Email sending
import smtplib
import sys
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders


# Get parameter and set constants
try:
    MODE = sys.argv[1]
except IndexError:
    MODE = 'TEST'
DB_FILE = 'login_file'
PDF_FORM = 'AOI_form.pdf'
EMAIL_SERVER = 'cernmx.cern.ch'
TESTER_EMAIL = 'Jozef.Podolec@cern.ch,Ivica.Dobrovicova@cern.ch'  # Use , as delimiter if more than one email


# Get credentials for database access from external file
def load_db_credentials():
    db_credentials = configparser.ConfigParser()
    db_credentials.read(DB_FILE)
    return db_credentials


# pdf handling
def _getFields(obj, tree=None, retval=None, fileobj=None):
    """
    Extracts field data if this PDF contains interactive form fields.
    The *tree* and *retval* parameters are for recursive use.

    :param fileobj: A file object (usually a text file) to write
        a report to on all interactive form fields found.
    :return: A dictionary where each key is a field name, and each
        value is a :class:`Field<PyPDF2.generic.Field>` object. By
        default, the mapping name is used for keys.
    :rtype: dict, or ``None`` if form data could not be located.
    """
    fieldAttributes = {
        '/FT': 'Field Type',
        '/Parent': 'Parent',
        '/T': 'Field Name',
        '/TU': 'Alternate Field Name',
        '/TM': 'Mapping Name',
        '/Ff': 'Field Flags',
        '/V': 'Value',
        '/DV': 'Default Value'
    }

    if retval is None:
        retval = OrderedDict()
        catalog = obj.trailer["/Root"]
        # get the AcroForm tree
        if "/AcroForm" in catalog:
            tree = catalog["/AcroForm"]
        else:
            return None
    if tree is None:
        return retval

    obj._checkKids(tree, retval, fileobj)
    for attr in fieldAttributes:
        if attr in tree:
            # Tree is a field
            obj._buildField(tree, retval, fileobj, fieldAttributes)
            break

    if "/Fields" in tree:
        fields = tree["/Fields"]
        for f in fields:
            field = f.getObject()
            obj._buildField(field, retval, fileobj, fieldAttributes)

    return retval


def get_form_fields(infile):
    infile = PdfFileReader(open(infile, 'rb'))
    fields = _getFields(infile)
    return OrderedDict((k, v.get('/V', '')) for k, v in fields.items())


def update_form_values(infile, outfile, newvals=None):
    pdf = PdfFileReader(open(infile, 'rb'))
    pdf.trailer["/Root"]["/AcroForm"].update(
        {NameObject("/NeedAppearances"): BooleanObject(True)}
    )
    writer = PdfFileWriter()
    trailer = pdf.trailer["/Root"]["/AcroForm"]
    writer._root_object.update({
        NameObject('/AcroForm'): trailer
    })

    for i in range(pdf.getNumPages()):
        page = pdf.getPage(i)
        try:
            if newvals:
                writer.updatePageFormFieldValues(page, newvals)

                for j in range(0, len(page['/Annots'])):
                    writer_annot = page['/Annots'][j].getObject()
                    for field in get_form_fields(infile):
                        if writer_annot.get('/T') == field:
                            writer_annot.update({
                                NameObject("/Ff"): NumberObject(1)  # make ReadOnly
                            })
            else:
                writer.updatePageFormFieldValues(page,
                                                 {k: f'#{i} {k}={v}'
                                                  for i, (k, v) in enumerate(get_form_fields(infile).items())
                                                  })
            writer.addPage(page)
        except Exception as e:
            print(repr(e))
            writer.addPage(page)

    with open(outfile, 'wb') as out:
        writer.write(out)


# ==========================
# ===== Main procedure =====
# ==========================
if __name__ == '__main__':
    print(">>>> Starting A/OI generation [" + formatdate(localtime=True) + "] <<<<")
    print("Mode = " + MODE)
    db_connection = None

    try:
        login_data = load_db_credentials()
    except:
        print("Error: Problem loading credentials")
        sys.exit(1)

    try:
        # Connect to the database
        db_connection = cx_Oracle.connect(login_data.get(MODE, "login"), login_data.get(MODE, "pwd"), login_data.get(MODE, "database"))
        update_cursor = db_connection.cursor()  # use this cursor for all updates within the loop

        with db_connection.cursor() as cursor:
            cursor.execute("select business_partner_id, address_code, date_of_last_aoi, eproc_enabled, new_aoi_date, "
                           "CERN_address_line1, CERN_address_line2, bp_address_name, bp_address, NVL(bp_tva_number, ' '), "
                           "email_from, replace(email_to,';',',') email_to, nvl(email_cc,' '), email_subject, email_body, "
                           "aoi_lieu_date, aoi_filled_form_name, bp_line1, bp_line2 "
                           "from AOI_TO_CREATE where email_to is not null ")

            for business_partner_id, address_code, date_of_last_aoi, eproc_enabled, new_aoi_date, \
                CERN_address_line1, CERN_address_line2, bp_address_name, bp_address, bp_tva_number, \
                email_from, email_to, email_cc, email_subject, email_body, aoi_lieu_date, aoi_filled_form_name,\
                bp_line1, bp_line2 in cursor:

                print(business_partner_id + "/" + address_code + "  (" + aoi_filled_form_name + ")")

                # Fill in the form
                update_form_values(PDF_FORM, f"filled_in_forms/{aoi_filled_form_name}",
                       {'Date d’émission': new_aoi_date,
                        'Le bénéficiaire institutionnel mentionné ci-après 1': CERN_address_line1,
                        'Le bénéficiaire institutionnel mentionné ci-après 2': CERN_address_line2,
                        'Lieu et date:': aoi_lieu_date,
                        'Nom et adresse du fournisseur, no TVA 1': bp_line1,
                        'Nom et adresse du fournisseur, no TVA 2': bp_line2})

                # Prepare email
                if MODE == 'TEST':
                    msg_to = TESTER_EMAIL
                    msg_cc = ' '
                    msg_bcc = ' '
                else:
                    msg_to = email_to
                    msg_cc = email_cc
                    msg_bcc = TESTER_EMAIL

                msg = MIMEMultipart()
                msg['From'] = email_from
                msg['To'] = msg_to
                msg['Cc'] = msg_cc
                # Do not add bcc here (otherwise you will reveal it)
                msg['Date'] = formatdate(localtime=True)
                msg['Subject'] = email_subject
                msg.attach(MIMEText(email_body))

                # Attach pdf to the email
                files = f"filled_in_forms/{aoi_filled_form_name}"  # Form to be attached
                part = MIMEBase('application', "octet-stream")
                with open(files, 'rb') as file:
                    part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment; filename="{}"'.format(Path(files).name))
                msg.attach(part)

                # Send email with its attachment
                # !!!Email delimiter must be ,
                all_recipients = msg['To'].split(",") + msg['Cc'].split(",") + msg_bcc.split(",")
                mail = smtplib.SMTP(EMAIL_SERVER)
                mail.sendmail(msg['From'], all_recipients, msg.as_string())
                print("Sent To:" + msg['To'] + " Cc:" + msg['Cc'] + " Bcc:" + msg_bcc)
                print(all_recipients)  # show how emails were parsed

                # Update the date in oetia when email was sent
                update_cursor.execute('update oetia set recoetia = :aoidate where tieoetia = :bpid and numoetia = :bpad',
                                      [new_aoi_date, business_partner_id, address_code])

                # Log the action in the database
                update_cursor.execute('insert into AOI_emails_sent (email_sent, bp_id, bp_ad, last_aoi_date, new_aoi_date, '
                                      'email_from, email_to, email_cc, email_subject, email_body) '
                                      'select sysdate, :1, :2, :3, :4, :5, :6, :7, :8, :9 from dual',
                                      [business_partner_id, address_code, date_of_last_aoi, new_aoi_date,
                                       email_from, email_to, email_cc, email_subject, email_body])
                db_connection.commit()

    except smtplib.SMTPException:
        print("Error: Unable to send email")
    except FileNotFoundError:
        print("Error: File Not Found")
    except cx_Oracle.Error as error:
        print(error)
    finally:
        if db_connection:
            db_connection.close()

print(">>>> Finished [" + formatdate(localtime=True) + "] <<<<\n\n")
