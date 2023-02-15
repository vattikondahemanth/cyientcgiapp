''' Login base page '''
import os
import delete_info_generator
q_string = os.environ['QUERY_STRING']

print(delete_info_generator.cgi_content())
print(delete_info_generator.cors_header())

#HTML Webpage
print(delete_info_generator.webpage_start())
print(delete_info_generator.webpage_head('Simple WebApp'))
print(delete_info_generator.webpage_body_start())
username = q_string.split("=")[1]
print(delete_info_generator.webpage_body(username))
print(delete_info_generator.webpage_body_end())
print(delete_info_generator.webpage_end())
