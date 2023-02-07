""" Home page generator """

import cgitb
cgitb.enable()

def cgi_content(re_type="text/html"):
    """ cgi_content """
    return 'Content type: ' + re_type + '\n\n'

def webpage_start():
    """ webpage_start """
    return '<html>'


def webpage_head(title):
    """ webpage_head """
    print("<head>")
    print(f"<title> {title} </title>")
    print('<meta http-equiv="refresh" content="3;url=http://localhost:8080/cgi-bin/home/home.py">') 
    print("</head>")

    return ""


def webpage_body_start():
    """ webpage_body_start """
    return "<body>"


def webpage_body(h1_message):
    """ body_start """
    print("<div align=\'right\'>")
    print("<a href=\"http://localhost:8080/cgi-bin/login/login.py\"> Login /</a>")
    print("<a href=\"http://localhost:8080/cgi-bin/login/signup.py\"> Sign Up </a>")
    print("</div>")
    return f'<h1 align="center"> {h1_message} </h1><p align="center">'

def webpage_body_end():
    """ body_end """
    return "</body>"

def webpage_end():
    """ webpage_end """
    return '</html>'
