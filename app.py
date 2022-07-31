import os
from read import get_json_reader
from write import load_db_table
import sys


# BASE_DIR = '/Users/chris/Documents/Python/research/data/retail_db_json'
# table_name = 'orders'
# con = 'postgresql://retail_user:retail_user@localhost:5452/retail_db'
#
# file_name = os.listdir(f'{BASE_DIR}/{table_name}')[0]
# file_path = f'{BASE_DIR}/{table_name}/{file_name}'

def process_table(BASE_DIR, con, table_name):
    json_reader = get_json_reader(BASE_DIR, table_name)
    for df in json_reader:
        load_db_table(df, con, table_name, df.columns[0])


def main():
    BASE_DIR = os.environ.get('BASE_DIR')
    table_names = sys.argv[1].split(',')
    configs = dict(os.environ.items())
    con = f'postgresql://{configs["DB_USER"]}:{configs["DB_PASS"]}@{configs["DB_HOST"]}:{configs["DB_PORT"]}/{configs["DB_NAME"]}'
    for table_name in table_names:
        process_table(BASE_DIR, con, table_name)


if __name__ == "__main__":
    main()