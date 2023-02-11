''' Employee info edit'''

import cgi
import mysql.connector

mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "root@123",
database = "cyientapp"
)

form = cgi.FieldStorage()

employee_id = form.getvalue("employeeid")
ph_number = form.getvalue("phnumber")
address = form.getvalue("address")
username = form.getvalue("username")

def update_employee_data():
    ''' Employee data Updating in sql '''

    cursor = mydb.cursor()
    
    update_sql = "UPDATE employee SET employeeid = %s, phnumber = %s, address = %s WHERE username = %s"
    values = (employee_id,ph_number,address,username)

    cursor.execute(update_sql, values)
    mydb.commit()

update_employee_data()