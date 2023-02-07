def cgi_content(type="text/html"):
	return('Content type: ' + type)

def cors_header():
	return('Access-Control-Allow-Origin: *')

def end_of_headers():
	return('\n\n')

def webpage_start():
	return('<html>')

def web_head_start():
	return ('<head>')

def bootstrap_css_ref():
	return ('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">')

def bootstrap_js_ref():
	return ('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>')

def jquery_ref():
	return ('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js"></script>')


def web_head_stop():
	return ('</head>')


def web_title(title):
	return('<title>' + title + '</title>')


def body_start():
	return('<body>')

def body_end():
	return("</body>")

def webpage_end():
	return('</html>')

def style_start():
	return ('<style>')

def style_end():
	return ('</style>')

def script_start():
	return ('<script>')

def script_end():
	return ('</script>')


def read_login_form():
	data = ""
	with open('cgi-bin/login/login.html', 'r') as f:
		data = f.read()
	return data


def login_page_script():
	data = ""
	with open('cgi-bin/login/login.js', 'r') as f:
		data = f.read()
	return data


def login_page_css():
	data = ""
	with open('cgi-bin/login/login.css', 'r') as f:
		data = f.read()
	return data
