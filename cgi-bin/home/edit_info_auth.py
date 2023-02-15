''' Edit Info Auth'''
import cgi
import cgitb
import os
import sys ; sys.path.append(os.getcwd() + '\\cgi-bin\\')
import mysql.connector

import edit_info_generator
import common.constant as const # pylint: disable=C0413,C0411,E0401

from  home import home_generator
cgitb.enable()

form = cgi.FieldStorage()
employee_id = form.getvalue("emp_id")
ph_number = form.getvalue("ph_num")
address = form.getvalue("address")
username = form.getvalue("email")

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "cyientapp"
    )

response = {"message":"", "status_code": const.HTTP_SERVER_ERROR}
cursor = mydb.cursor()
cursor.execute("SELECT * FROM employee WHERE username=%s;", (username,))
db_username = cursor.fetchone()

if db_username and username in db_username:
    update_sql = "UPDATE employee SET employeeid = %s, phnumber = %s, address = %s WHERE username = %s;"
    values = (employee_id,ph_number,address,username)
    cursor.execute(update_sql, values)
    cursor.close()
    mydb.commit()
    mydb.close()

    response["status_code"] = const.HTTP_SUCCESS
    response["message"] = "Successfully Updated"

else:
    response["status_code"] = const.HTTP_BAD_REQUEST
    response["message"] = "Bad Request"

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
