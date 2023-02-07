import os
import sys ; sys.path.append(os.getcwd() + '\\cgi-bin\\')
import cgi

import login_generator


form = cgi.FieldStorage()


print(login_generator.cgi_content())
print(login_generator.cors_header())
print(login_generator.end_of_headers())




print(login_generator.webpage_start())
print(login_generator.web_title('Cyient WebApp'))
print(login_generator.web_head_start())

print(login_generator.bootstrap_css_ref())
print(login_generator.jquery_ref())
print(login_generator.bootstrap_js_ref())


print(login_generator.style_start())
print(login_generator.login_page_css())
print(login_generator.style_end())

print(login_generator.web_head_stop())


print(login_generator.body_start())


redirectURL = "http://localhost:8080/cgi-bin/home/home.py"
print('<meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 


print(login_generator.body_end())

print(login_generator.webpage_end())
