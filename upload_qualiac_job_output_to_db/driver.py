import sys

from utils import log, file_exists, file_exists_in_db, get_db_connection, insert_file_in_db

if __name__ == '__main__':
    MODE = sys.argv[1] if len(sys.argv) >= 2 else 'TEST'

    log('copying purchase orders from Qualiac to db')
    log(f'Env={MODE}')

    db_connection = get_db_connection()

    with db_connection.cursor() as cursor:
        cursor.execute("select infoid, infomessage from infolog where infotype = 'ORDERSPRINTED'")
        files_migrated = 0
        files_not_found_on_qualiac_server = 0
        total_files = 0

        for file_id, file_path in cursor:
            total_files += 1
            if not file_exists(file_path):
                log(f'{file_path} does not exist on qualiac server')
                files_not_found_on_qualiac_server += 1
                continue

            if file_exists_in_db(file_id):
                # delete_file_from_infolog_table(file_id)
                continue

            insert_file_in_db(file_id, file_path)
            files_migrated += 1

    db_connection.close()
    log(f'{files_migrated} files moved to DB')
    log(f'{total_files - files_migrated - files_not_found_on_qualiac_server} files already existed on db server')
    if files_not_found_on_qualiac_server > 0:
        log(f'{files_not_found_on_qualiac_server} files were present in infolog, but not present on qualiac server')
