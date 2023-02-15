''' Edit Info Page '''
import os
import edit_info_generator

import mysql.connector

q_string = os.environ['QUERY_STRING']

print(edit_info_generator.cgi_content())
print(edit_info_generator.cors_header())

#HTML Webpage
print(edit_info_generator.webpage_start())
print(edit_info_generator.webpage_head('Simple WebApp'))
print(edit_info_generator.webpage_body_start())

emplist = list()
if q_string:
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "cyientapp"
    )
    username = q_string.split("=")[1]
    cursor = mydb.cursor()
    query = "SELECT employeeid,username,phnumber,address FROM employee WHERE username = %s;"
    cursor.execute(query, (username, ))
    emplist = list(cursor)
    cursor.close()
    mydb.close()

print(edit_info_generator.webpage_edit_body(emplist))
print(edit_info_generator.webpage_body_end())
print(edit_info_generator.webpage_end())


