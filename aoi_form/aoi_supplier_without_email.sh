#!/bin/bash

mailto="Ivica.Dobrovicova@cern.ch"

a=`$ORACLE_HOME/bin/sqlplus @/usr/cern/sql/aoi_supplier_without_email.sql`

if echo $a|egrep -i 'Error' >/dev/null; then
# Failed
        (
        echo
        echo The following is an output of aisjobs:/usr/cern/unixScripts/aoi_form/aoi_supplier_without_email.sh
        echo
        echo $a
        echo
        echo
         )|/bin/mail -s "ERROR problem sending email: aoi_supplier_without_email.sh" $mailto
#else
#Succeeded
#       (
#        echo
#        echo The following is an output of dbsrvd203:/usr/cern/unixScripts/stuckorders11.sh
#        echo
#        echo $a
#        echo
#        echo
 #        )|/bin/mail -s "stuckorders11" $mailto
fi
