import sqlite3
import pandas as pd

conn=sqlite3.connect("payroll.db")
cursor=conn.cursor()
# here we create a dept table columns dno int primary key auto increament,dname text, loc text
# primary key is a contraint that restrict duplicate and null values

cursor.execute('''
CREATE TABLE IF NOT EXISTS dept (
    dno INTEGER PRIMARY KEY AUTOINCREMENT,
    dname TEXT not null,
    loc TEXT
)
''')

conn.commit()
conn.close()

def create_dept(dname, loc):
    conn = sqlite3.connect("payroll.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO dept (dname, loc) VALUES (?, ?)", (dname, loc))
    conn.commit()
    conn.close()

def read_dept():
    conn = sqlite3.connect("payroll.db")
    df=pd.read_sql_query("SELECT * FROM dept", conn)
    conn.close()
    return df

def update_dept(dno, dname, loc):
    conn = sqlite3.connect("payroll.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE dept SET dname = ?, loc = ? WHERE dno = ?", (dname, loc, dno))
    conn.commit()
    conn.close()

def delete_dept(dno):
    conn = sqlite3.connect("payroll.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM dept WHERE dno = ?", (dno,))
    conn.commit()
    conn.close()

while True:
    print("\nDepartment Management System")
    print("1. Create Department")
    print("2. Read Departments")
    print("3. Update Department")
    print("4. Delete Department")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        dname = input("Enter department name: ")
        loc = input("Enter location: ")
        create_dept(dname, loc)
        print("Department created successfully.")
    elif choice == '2':
        departments = read_dept()
        print(departments)
        
    elif choice == '3':
        dno = int(input("Enter department number to update: "))
        dname = input("Enter new department name: ")
        loc = input("Enter new location: ")
        update_dept(dno, dname, loc)
        print("Department updated successfully.")
    elif choice == '4':
        dno = int(input("Enter department number to delete: "))
        delete_dept(dno)
        print("Department deleted successfully.")
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")