''' signup base page '''

import signup_generator


print(signup_generator.cgi_content())

#HTML Webpage
print(signup_generator.webpage_start())
print(signup_generator.webpage_head('Simple WebApp'))
print(signup_generator.webpage_body_start())
print(signup_generator.webpage_body())
print(signup_generator.webpage_body_end())
print(signup_generator.webpage_end())
