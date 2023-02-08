''' Login base page '''
import os
import login_generator
q_string = os.environ['QUERY_STRING']

print(login_generator.cgi_content())
print(login_generator.cors_header())

#HTML Webpage
print(login_generator.webpage_start())
print(login_generator.webpage_head('Simple WebApp'))
print(login_generator.webpage_body_start())
print(login_generator.webpage_body())

if q_string.split("=")[1] == "401":
    print(login_generator.response({"message":"Password not valid"}))
elif q_string.split("=")[1] == "404":
    print(login_generator.response({"message":"User name is not found"}))
elif q_string.split("=")[1] == "500":
    print(login_generator.response({"message":"Server encountered an issue"}))


print(login_generator.webpage_body_end())
print(login_generator.webpage_end())
