'''Home Page Profile'''
import mysql.connector

mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "root@123",
database = "cyientapp"

)

def employee_data():
    ''' Employee data extracting from sql '''
    cursor = mydb.cursor()

    query = "SELECT employeeid,username,phnumber,address FROM employee;"

    cursor.execute(query)
    emplist = []
    for data in cursor:
        emplist.append(data)

    cursor.close()
    return emplist
