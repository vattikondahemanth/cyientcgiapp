''' Employee info delete'''
import cgi
import cgitb
import os
import sys ; sys.path.append(os.getcwd() + '\\cgi-bin\\')
import mysql.connector
import delete_info_generator
import common.constant as const # pylint: disable=C0413,C0411,E0401
from home import home_generator
cgitb.enable()

form = cgi.FieldStorage()
username = form.getvalue("username")

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
response["db_username"] = db_username

if db_username and username in db_username:
    sql_query = "DELETE FROM employee WHERE username = %s"
    cursor.execute(sql_query, (username,))
    mydb.commit()
    cursor.close()
    mydb.close()
    response["message"] = "Deleted Successfully"
    response["status_code"] = const.HTTP_DELETED_SUCCESSFULLY
else:
    response["message"] = "Bad Request"
    response["status_code"] = const.HTTP_BAD_REQUEST

if response["status_code"] == 202:
    print(home_generator.cgi_content())
    print(home_generator.cors_header())

    #HTML Webpage
    print(home_generator.webpage_start())
    print(home_generator.webpage_head('Simple WebApp'))
    print(home_generator.webpage_body_start())
    print(home_generator.webpage_body())
    print('<meta http-equiv="refresh" content="0;url=http://localhost:8080/cgi-bin/home/home.py">')
    print(response)
    print(home_generator.webpage_body_end())
    print(home_generator.webpage_end())
