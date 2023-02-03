''' Login base page '''
import login_generator


print(login_generator.cgi_content())

#HTML Webpage
print(login_generator.webpage_start())
print(login_generator.webpage_head('Simple WebApp'))
print(login_generator.webpage_body_start())
print(login_generator.webpage_body())
print(login_generator.webpage_body_end())
print(login_generator.webpage_end())
