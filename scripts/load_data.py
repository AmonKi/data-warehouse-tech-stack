import csv
import MySQLdb
import pandas as pd

mydb = MySQLdb.connect(host='127.0.0.1',
    user='root',
    passwd='kymtai961',
    db='trial')
cursor = mydb.cursor()

csv_data = pd.read_csv('/home/amon/Downloads/trial.csv')
for row in csv_data:

    cursor.execute('INSERT INTO kim(name, gender, \
          age, location )' \
          'VALUES("%s", "%s", "%s")', 
          row)
#close the connection to the database.
mydb.commit()
cursor.close()
print ("Done")