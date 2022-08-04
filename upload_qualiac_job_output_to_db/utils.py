import os.path

__all__ = [
    'formatted_time_stamp',
    'log',
    'file_exists',
    'file_exists_in_db',
    'get_db_connection',
    'insert_file_in_db'
]

from email.utils import formatdate
import configparser
import cx_Oracle
import datetime

DB_FILE = 'login_file'


def formatted_time_stamp() -> str:
    return formatdate(localtime=True)


def log(message='') -> None:
    print(f'[{formatted_time_stamp()}] {message}')


def load_db_credentials():
    db_credentials = configparser.ConfigParser()
    db_credentials.read(DB_FILE)
    return db_credentials


def file_exists(file_path: str) -> bool:
    return os.path.exists(file_path)


def file_exists_in_db(file_name: str) -> bool:
    db_connection = get_db_connection()
    with db_connection.cursor() as cursor:
        cursor.execute(f"""select count(*) 
            from infolog 
            where infotype = 'ORDERSPRINTED'
            and infoid = '{file_name}'
        """)

        return cursor.fetchall()[0][0] > 0


def get_db_connection(env='TEST'):
    login_data = load_db_credentials()
    return cx_Oracle.connect(login_data.get(env, "login"), login_data.get(env, "pwd"),
                             login_data.get(env, "database"))


def insert_file_in_db(file_id, file_path) -> None:
    file = open(file_path, 'rb')
    file_content = file.read()
    creation_date = datetime.datetime.now()
    db_connection = get_db_connection()

    with db_connection.cursor() as db_writer:
        db_writer.execute(
            "insert into po_printed_file values (:file_id, :file_path, :file_content, :creation_date, 'N', null)",
            [file_id, file_path, file_content, creation_date])

        db_connection.commit()
        db_writer.close()
