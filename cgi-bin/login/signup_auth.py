''' Sign Up Auth'''
import cgi
import cgitb
import os
import sys ; sys.path.append(os.getcwd() + '\\cgi-bin\\')
import mysql.connector

from  home import home_generator
import signup_generator
import common.constant as const

cgitb.enable()


form = cgi.FieldStorage()
username = form.getvalue("email")
password = form.getvalue("pswd")
re_password = form.getvalue("psw_repeat")

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root@123",
    database = "cyientapp"
    )

response = {"message":"", "status_code": const.HTTP_SERVER_ERROR}

cursor = mydb.cursor()
cursor.execute(f"SELECT username FROM employee WHERE username = \"{username}\";")
db_username = cursor.fetchone()

if not db_username:
    if re_password == password:
        try:

            cursor.execute(f"""INSERT INTO employee (username, password)
                            VALUES (\"{username}\", \"{password}\");""")
            response["message"] = "User Created Successfully"
            response["status_code"] = const.HTTP_SUCCESS
        except:
            response["message"] = "Server Error"
            response["status_code"] = const.HTTP_SERVER_ERROR

    else:
        response["message"] = "Password not matched"
        response["status_code"] = const.HTTP_INFORMATION
else:
    response["message"] = "User Already Exits"
    response["status_code"] = const.HTTP_INFORMATION

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

    print(signup_generator.cgi_content())
    print(signup_generator.cors_header())

    #HTML Webpage
    print(signup_generator.webpage_start())
    print(signup_generator.webpage_head('Simple WebApp'))
    print(signup_generator.webpage_body_start())
    print(signup_generator.webpage_body())
    print(signup_generator.webpage_body_end())
    print(signup_generator.webpage_end())
