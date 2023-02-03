''' Reset password page '''

import reset_password_generator


print(reset_password_generator.cgi_content())

#HTML Webpage
print(reset_password_generator.webpage_start())
print(reset_password_generator.webpage_head('Simple WebApp'))
print(reset_password_generator.webpage_body_start())
print(reset_password_generator.webpage_body())
print(reset_password_generator.webpage_body_end())
print(reset_password_generator.webpage_end())
