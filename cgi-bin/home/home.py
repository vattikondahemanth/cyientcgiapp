""" Home Page """

import home_generator

print(home_generator.cgi_content())

#HTML Webpage
print(home_generator.webpage_start())
print(home_generator.webpage_head('Simple WebApp'))
print(home_generator.webpage_body_start())
print(home_generator.webpage_body())
print(home_generator.webpage_body_end())
print(home_generator.webpage_end())
