""" Home Page """

import home_generator


print(home_generator.cgi_content())

#HTML Webpage
print(home_generator.webpage_start())
print(home_generator.web_title('Simple WebApp'))
print(home_generator.body_start('This is Home Page '))
print(home_generator.body_end())
print(home_generator.webpage_end())
