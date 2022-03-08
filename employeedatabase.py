import sqlite3
connection=sqlite3.connect("company.db")


# connection.execute('''CREATE TABLE EMPLOYEE(
# ID INTEGER PRIMARY KEY AUTOINCREMENT,
# NAME TEXT,
# DESIGNATION TEXT,
# SALARY INTEGER,
# COMPANY_NAME TEXT,
# MOBILE INT);
# ''')
# print("Table created successfully Ramya!!!!!")


getName=input("Enter name: ")
getDes=input("Enter designation: ")
getSalary=input("Enter the salary")
getCompanyname=input("Enter companyname")
getMobile=input("Enter mobileNumber")

connection.execute("INSERT INTO EMPLOYEE(NAME,DESIGNATION,SALARY,COMPANY_NAME,MOBILE)\
                   VALUES('"+getName+"','"+getDes+"',"+getSalary+",'"+getCompanyname+"',"+getMobile+")")
connection.commit()
connection.close()
print("success!")