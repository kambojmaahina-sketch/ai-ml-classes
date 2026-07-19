import sqlite3

# create the conection object
# connect function check the db file if it is not present then
# it will create a new db file
conn=sqlite3.connect("payroll.db")

#create the curdor object
#it is respondible for create,read,update and delete operations(CRUD)
cursor=conn.cursor()

print("Database created and successfully connected to SQLite")
#never forget to close the connection
conn.close()