''' Login Auth'''

import cgi
import shutil

import mysql.connector

import login_generator


common_path = "cgi-bin/common/"
current_path = "cgi-bin/login/common"
shutil.copytree(common_path, current_path)

import common.constant as const # pylint: disable=C0413,C0411,E0401

form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("password")

username = "Vijaya"
password= "Vijaya@123"

mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "root@123",
database = "cyientapp"
)

response = {"message":"", "status_code": const.HTTP_SERVER_ERROR}

cursor = mydb.cursor()

cursor.execute("SELECT username FROM employee WHERE username=%s", (username,))

db_username = cursor.fetchone()

if db_username[0] == username:

    cursor.execute("SELECT password FROM employee WHERE username = %s", (username,))

    row = cursor.fetchone()

    mydb.close()

    if row and row[0] == password:
        response["message"] = "Authentication Success"
        response["status_code"] = const.HTTP_SUCCESS

    else:
        response["message"] = "Authentication Failed"
        response["status_code"] = const.HTTP_AUTH_FAIL

else:
    response["message"] = "Username is not registered"
    response["status_code"] = const.HTTP_RESOURCE_NOT_FOUND

print(response)




print(login_generator.cgi_content())

#HTML Webpage
print(login_generator.webpage_start())
print(login_generator.web_title('Simple WebApp'))
print(login_generator.body_start(''))
print(response)
print(login_generator.body_end())
print(login_generator.webpage_end())

shutil.rmtree(current_path)
