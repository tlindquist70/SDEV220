#SDEV220_10P_M04_ProgrammingAssignment
#16.8
#Use sqlalchemy to connect to sqlite3 books.db
#select and print the title column from the book table in alphabetical order


import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Numeric, Integer, VARCHAR, text
from sqlalchemy.engine import result

#test connection to flask
print("attempting to connect")

#connect to database
conn = create_engine('sqlite:///instance/data.db') 
#sql script query the book database and to return book titles in alphabetical order
sql = 'select book_name from book order by book_name asc'
with conn.engine.connect() as connection:
    rows = connection.execute(text(sql))  
    connection.commit()


#print query results    
    for row in rows: 
        print(row)
