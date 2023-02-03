""" Home page generator """


def cgi_content(re_type="text/html"):
    """ cgi_content """
    return 'Content type: ' + re_type + '\n\n'

def webpage_start():
    """ webpage_start """
    return '<html>'


def web_title(title):
    """ web_title """
    return '<head><title>' + title + '</title></head>'

def body_start(h1_message):
    """ body_start """
    print("<div align=\'right\'>")
    print("<a href=\"http://127.0.0.1:8080/cgi-bin/login/login.py\"> Login /</a>")
    print("<a href=\"http://127.0.0.1:8080/cgi-bin/login/signup.py\"> Sign Up </a>")
    print("</div>")
    return '<h1 align="center">' + h1_message + '</h1><p align="center">'

def body_end():
    """ body_end """
    return "</body>"

def webpage_end():
    """ webpage_end """
    return '</html>'
