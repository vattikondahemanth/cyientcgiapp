''' Employee info delete'''

import cgi
import mysql.connector

mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "root@123",
database = "cyientapp"
)

# get the form data
form = cgi.FieldStorage()
username = form.getvalue("username")

def delete_employee_data():
    ''' Employee data delete from sql '''

    cursor = mydb.cursor()

    sql_query = "DELETE FROM employee WHERE username = %s"
    cursor.execute(sql_query, (username,))

    mydb.commit()

    cursor.close()
    mydb.close()

delete_employee_data()
