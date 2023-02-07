''' Login Auth'''
import os
import sys ; sys.path.append(os.getcwd() + '\\cgi-bin\\')
import cgi
import cgitb
import mysql.connector
from  home import home_generator
import common.constant as const # pylint: disable=C0413,C0411,E0401

cgitb.enable()


form = cgi.FieldStorage()
username = form.getvalue("email")
password = form.getvalue("pswd")

# username = "vijay@abc.com"
# password= "vijay"

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "cyientapp"
    )

response = {"message":"", "status_code": const.HTTP_SERVER_ERROR}

cursor = mydb.cursor()
cursor.execute("SELECT username FROM employee WHERE username=%s;", (username,))
db_username = cursor.fetchone()

if db_username and username in db_username:
    cursor.execute("SELECT password FROM employee WHERE username = %s;", (username,))
    row = cursor.fetchone()
    if row and row[0] == password:
        response["message"] = "Authentication Success"
        response["status_code"] = const.HTTP_SUCCESS
    else:
        response["message"] = "Password Authentication Failed"
        response["status_code"] = const.HTTP_AUTH_FAIL
else:
    response["message"] = "Username is not registered"
    response["status_code"] = const.HTTP_RESOURCE_NOT_FOUND

cursor.close()

if response["message"] == 200:
    print("Location: http://localhost:8080/cgi-bin/home/home.py")

print('<meta http-equiv="refresh" content="0;url=http://localhost:8080/cgi-bin/home/home.py">')
print(home_generator.cgi_content())

#HTML Webpage
print(home_generator.webpage_start())
print(home_generator.webpage_head('Simple WebApp'))
print(home_generator.webpage_body_start())
print(home_generator.webpage_body('This is Home Page '))
print(home_generator.webpage_body_end())
print(home_generator.webpage_end())
