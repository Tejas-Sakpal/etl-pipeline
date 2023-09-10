"""
Description: Script to load the data on Postgresql.
"""
from transform import transform
import psycopg2


def load():
    """
    Description: Method to load dataframe to Postgresql.
    Input: None
    Output: None
    """

    conn = psycopg2.connect(database = "postgres",  user = "postgres", host= 'localhost', password = "pass123",port = 5432) 
    data_frame = transform()
    cur = conn.cursor()
    table_name = 'sales_wa'
    create_table = f"CREATE TABLE IF NOT EXISTS {table_name} ("
    for col_name, col_dtype in zip(data_frame.columns, data_frame.dtypes):
         
         if str(col_dtype) == 'object':  
            postgres_dtype = 'VARCHAR'
         elif 'int' in str(col_dtype): 
            postgres_dtype = 'INTEGER'
         elif 'float' in str(col_dtype):   
            postgres_dtype = 'FLOAT'
         else: 
            postgres_dtype = 'VARCHAR'  
    
         create_table += f"{col_name} {postgres_dtype}, "
    create_table = create_table.rstrip(', ') + ");"
    cur.execute(create_table)
    for row in data_frame.itertuples(index=False):
        insert_sql = f"INSERT INTO {table_name} VALUES ({', '.join(['%s' for _ in range(len(row))])});"
        cur.execute(insert_sql, row)
    conn.commit()






