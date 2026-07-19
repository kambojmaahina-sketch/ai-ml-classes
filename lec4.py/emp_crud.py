# employee table
# empid, ename, job, sal, dno
# perform crud operations on employee table

import sqlite3
import pandas as pd

conn=sqlite3.connect("employee.db")
cursor=conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS emp (
    empid INTEGER PRIMARY KEY AUTOINCREMENT,
    ename TEXT not null,
    job TEXT NOT NULL,
    sal INTEGER NOT NULL,
    dno INTEGER NOT NULL
)
''')

conn.commit()
conn.close()

def create_emp(ename,job,sal,dno):
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO emp (ename, job, sal, dno) VALUES (?, ?, ?, ?)",
        (ename, job, sal, dno)
    )
    conn.commit()
    conn.close()

def read_emp():
    conn = sqlite3.connect("employee.db")
    df=pd.read_sql_query("SELECT * FROM emp", conn)
    conn.close()
    return df

def update_emp(empid, ename, job):
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE emp SET ename = ?, job = ? WHERE empid = ?", (empid, ename, job))
    print("Rows updated:", cursor.rowcount)
    conn.commit()
    conn.close()

def delete_emp(empid):
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM emp WHERE empid = ?", (empid,))
    conn.commit()
    conn.close()

while True:
    print("\nEmployee Management System")
    print("1. Create Employee")
    print("2. Read Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        ename = input("Enter employee name: ")
        job = input("Enter job: ")
        sal = int(input("Enter salary: "))
        dno = int(input("Enter department number: "))
        create_emp(ename, job, sal, dno)
        print("Employee created successfully.")
    elif choice == '2':
        employees = read_emp()
        print(employees)
    elif choice == '3':
        empid = int(input("Enter Employee number to update: "))
        ename = input("Enter new Employee name: ")
        job = input("Enter new job: ")
        update_emp(empid, ename,job )
        print("Employee updated successfully.")
    elif choice == '4':
        empid = int(input("Enter Employee id to delete: "))
        delete_emp(empid)
        print("Employee deleted successfully.")
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")