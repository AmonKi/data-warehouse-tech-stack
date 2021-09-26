import csv
import pandas as pd
from sqlalchemy import create_engine, types

engine = create_engine('mysql://root:Kymtai96!@localhost/trial') # enter your password and database names here

df = pd.read_csv("/home/amon/Downloads/trial.csv",sep=',',quotechar='\'',encoding='utf8') # Replace Excel_file_name with your excel sheet name
df.to_sql('kim',con=engine,index=False,if_exists='append') # Replace Table_name with your sql table name