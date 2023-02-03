''' signup base page generator'''

import cgi



def cgi_content(re_type="text/html"):
    """ cgi_content """
    return 'Content type: ' + re_type + '\n\n'

def webpage_start():
    """ webpage_start """
    return "<html>"

def webpage_head(title):
    """ webpage_head """
    print("<head>")
    print(f"<title> {title} </title>")
    print("<meta charset=\"utf-8\">")
    print("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">")
    print("""<link rel=\"stylesheet\" href=\"https://cdn.jsdelivr.net/npm/bootstrap@4.6.2
            /dist/css/bootstrap.min.css\">""")
    print("""<script src=\"https://cdn.jsdelivr.net/npm/jquery@3.6.1/dist/jquery.slim.min.js\">
            </script>""")
    print("""<script src=\"https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js\">
            </script>""")
    print("""<script src=\"https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/
            bootstrap.bundle.min.js\"></script>""")
    print("</head>")
    return ""

def webpage_body_start():
    """ webpage_body_start """
    return "<body>"

def webpage_body():
    """ webpage_body """
    form = cgi.FieldStorage()
    print("<div class=\"container border border-secondary rounded float-justify mt-4 \" ")
    print("<div class=\"card\" style=\"width:500px\" >")
    print("""<div class=\"card-header \" align=\"center\" >&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
        &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
        &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp    Sign Up   
        &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
        &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp 
        <a href=\"login.py\"> Login </a> 
        <p> Please fill in this form to create an account. </p> </div>""")
    print("<form action=\"/action_page.php\" class=\"card-body\" >")
    print("<div class=\"form-group\">")
    print("<label for=\"email\">Email / Name:</label>")
    print("""<input type=\"email\" class=\"form-control\"
            id=\"email\" placeholder=\"Enter email / name\" name=\"email\">""")
    print("</div>")
    print("<div class=\"form-group\">")
    print("<label for=\"pwd\">Password:</label>")
    print("""<input type=\"password\" class=\"form-control\"
            id=\"pwd\" placeholder=\"Enter password\" name=\"pswd\">""")
    print("</div>")
    print("<div class=\"form-group\">")
    print("<label for=\"psw-repeat\">Repeat Password:</label>")
    print("""<input type=\"password\" class=\"form-control\"
            id=\"psw-repeat\" placeholder=\"Repeat Password\" name=\"pswd\">""")
    print("</div>")
    print("<div class=\"form-group form-check\">")
    print("<label class=\"form-check-label\">")
    print("<input class=\"form-check-input\" type=\"checkbox\" name=\"remember\"> Remember me")
    print("</label>")
    print("</div>")
    print("</form>")
    print("<div class=\"card-footer\" align=\"center\" >")
    print("<button type=\"submit\" class=\"btn btn-primary\">Sign Up</button>")
    print("""<button type=\"button\" class=\"btn btn-danger\">
            <a href=\"http://127.0.0.1:8080/cgi-bin/home/home.py\"> Cancel </a></button>""")
    # print("<button type=\"button\" class=\"btn btn-danger\">Cancel</button>")
    print("</div>")
    print("</div>")
    print("</div>")
    print("</div>")
    return ""

def webpage_body_end():
    """ webpage_body_end """
    return "</body>"

def webpage_end():
    """ webpage_end """
    return "</html>"
