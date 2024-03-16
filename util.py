import pandas as pd

def get_tables(path):
    tables = pd.read_csv(path, sep=":")
    # print("Loaded DataFrame:\n", tables)

    return tables.query('to_be_loaded == "yes"')