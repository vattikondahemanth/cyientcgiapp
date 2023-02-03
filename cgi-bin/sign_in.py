''' database Config '''

import cgi
import mysql.connector

form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("password")

# username = "Sumant"
# password = "Sumant@123"

mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "root@123",
database = "cyientapp"
)

cursor = mydb.cursor()

cursor.execute("SELECT username FROM employee WHERE username=%s", (username,))

username = cursor.fetchone()

if username is not None:
    print("User already exist, Please enter unique username")

else:
    cursor.execute("INSERT INTO employee (username, password) VALUES (%s, %s)",
        (username, password))
    mydb.commit()
    mydb.close()

    print("Username and Password Inserted")
