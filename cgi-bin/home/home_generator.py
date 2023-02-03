def cgi_content(type="text/html"):
	return('Content type: ' + type + '\n\n')

def webpage_start():
	return('<html>')


def web_title(title):
	return('<head><title>' + title + '</title></head>')

def body_start(h1_message):
	print("<div align=\'right\'>")
	print("<a href=\"http://127.0.0.1:8080/cgi-bin/login/login.py\"> Login /</a>")
	print("<a href=\"http://127.0.0.1:8080/cgi-bin/login/signup.py\"> Sign Up </a>")
	print("</div>")
	return('<h1 align="center">' + h1_message + '</h1><p align="center">')

def body_end():
	return("</body>")

def webpage_end():
	return('</html>')