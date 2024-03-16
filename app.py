import sys
from config import DB_DETAILS
from util import get_tables

def main():
    try:
        env = sys.argv[1]
    except IndexError:
        print("No environment provided. Defaulting to 'dev'.")
        env = 'dev'  # default parameter
    db = DB_DETAILS[env]
    tables = get_tables('table_list.txt')
    # for idx, table in tables.iterrows():
    #only output table name
    for table in tables['table_name']:
        print(table)
if __name__ == '__main__':
    main()
