import login_generator


print(login_generator.cgi_content())

#HTML Webpage
print(login_generator.webpage_start())
print(login_generator.web_title('Simple WebApp'))
print(login_generator.body_start('This is Login Page '))
print(login_generator.body_end())
print(login_generator.webpage_end())