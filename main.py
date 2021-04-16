import numpy as np
import pandas as pd
import sqlite3
from sqlalchemy import create_engine
DIR = './Data'
FILE = '/products.csv'

file = '{}{}'.format(DIR, FILE)

print('File Directory: {}'.format(file))
print(pd.read_csv(file, nrows=2))
print(pd.read_csv(file))

csv_database = create_engine('sqlite:///csv_database.db')

chunksize = 10000
i = 0
j = 0

for df in pd.read_csv(file, chunksize = chunksize, iterator = True):
    df = df.rename(columns = {c: c.replace (' ', '') for c  in df.columns})
    df.index +=3
    
    df.to_sql('data_use', csv_database, if_exists = 'append')
    j = df.index[-1]+1
    
    print('| index : {}'.format(j))

df = pd.read_sql_query('SELECT DISTINCT name,sku,description FROM data_use ORDER BY sku', csv_database)
df.columns
df.head(10)
