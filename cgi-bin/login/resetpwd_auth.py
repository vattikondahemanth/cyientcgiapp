''' Reset Password Auth'''
import cgi
import cgitb
import os
import sys ; sys.path.append(os.getcwd() + '\\cgi-bin\\')
import mysql.connector

from  home import home_generator
import reset_password_generator
import common.constant as const

cgitb.enable()


form = cgi.FieldStorage()
username = form.getvalue("email")
old_password = form.getvalue("pwd_old")
new_password = form.getvalue("pwd_new")
new_re_password = form.getvalue("pwd_new_repeat")

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "cyientapp"
    )

form_data = {

    "username" : username,
    "old_password" : old_password,
    "new_password" : new_password,
    "new_re_password" : new_re_password
    }
response = {"message":"", "status_code": const.HTTP_SERVER_ERROR}

cursor = mydb.cursor(buffered=True)
cursor.execute(f"SELECT username FROM employee WHERE username = \"{username}\";")
db_username = cursor.fetchone()

if db_username:
    cursor.execute(f"SELECT password FROM employee WHERE username = \"{username}\";")
    db_pwd = cursor.fetchone()
    if old_password == db_pwd[0]:
        if new_password == new_re_password:
            try:
                cursor.execute(f"""UPDATE employee SET password = \"{new_password}\"
                                WHERE (username = \"{username}\"); """)
                response["message"] = "Password Reset Successfull"
                response["status_code"] = const.HTTP_SUCCESS
            except:
                response["message"] = "Server Error"
                response["status_code"] = const.HTTP_SERVER_ERROR
        else:
            response["message"] = "New Password not matched"
            response["status_code"] = const.HTTP_INFORMATION
    else:
        response["message"] = "Old Password not matched"
        response["status_code"] = const.HTTP_INFORMATION
else:
    response["message"] = "Username is not registered"
    response["status_code"] = const.HTTP_INFORMATION

cursor.close()
mydb.commit()
mydb.close()

print(home_generator.cgi_content())
print(home_generator.cors_header())

#HTML Webpage
print(home_generator.webpage_start())
print(home_generator.webpage_head('Simple WebApp'))
print(home_generator.webpage_body_start())
print(home_generator.webpage_body())
print(home_generator.webpage_body_end())
print(home_generator.webpage_end())
