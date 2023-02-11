''' Login Auth'''
import cgi
import cgitb
import os
import sys ; sys.path.append(os.getcwd() + '\\cgi-bin\\')
import mysql.connector

import login_generator
import common.constant as const # pylint: disable=C0413,C0411,E0401

from home import home_generator

cgitb.enable()

form = cgi.FieldStorage()
username = form.getvalue("email")
password = form.getvalue("pswd")

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root@123",
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
    response["message"] = "User Name is not registered"
    response["status_code"] = const.HTTP_RESOURCE_NOT_FOUND

cursor.close()
mydb.commit()
mydb.close()

if response["status_code"] == 200:
    print(home_generator.cgi_content())
    print(home_generator.cors_header())

    #HTML Webpage
    print(home_generator.webpage_start())
    print(home_generator.webpage_head('Simple WebApp'))
    print(home_generator.webpage_body_start())
    print(home_generator.webpage_body())
    print('<meta http-equiv="refresh" content="0;url=http://localhost:8080/cgi-bin/home/home.py">')
    print(home_generator.webpage_body_end())
    print(home_generator.webpage_end())

else:
    print(login_generator.cgi_content())
    print(login_generator.cors_header())

    #HTML Webpage
    print(login_generator.webpage_start())
    print(login_generator.webpage_head('Simple WebApp'))
    print(login_generator.webpage_body_start())
    print(login_generator.webpage_body())
    print(f"""<meta http-equiv="refresh" content="0;
            url=http://localhost:8080/cgi-bin/login/login.py?error={response["status_code"]}">""")
    print(login_generator.webpage_body_end())
    print(login_generator.webpage_end())
