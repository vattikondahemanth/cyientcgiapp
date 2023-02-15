''' signup base page '''
import cgi
import os
import signup_generator
q_string = os.environ['QUERY_STRING']


print(signup_generator.cgi_content())
print(signup_generator.cors_header())

#HTML Webpage
print(signup_generator.webpage_start())
print(signup_generator.webpage_head('Simple WebApp'))
print(signup_generator.webpage_body_start())

if q_string:
    if q_string.split("=")[1] == "400":
        print(signup_generator.response({"message":"Bas Request"}))

print(signup_generator.webpage_body())
print(signup_generator.webpage_body_end())
print(signup_generator.webpage_end())
