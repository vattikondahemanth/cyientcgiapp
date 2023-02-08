''' signup base page generator'''

def cgi_content(re_type="text/html"):
    """ cgi_content """
    return 'Content type: ' + re_type + '\n\n'


def cors_header():
    """ cors_header """
    return 'Access-Control-Allow-Origin: *' + '\n\n'

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

    #Click the radio button to toggle between password visibility:
    print("<script>")
    print("function myFunction() {")
    print("var x = document.getElementById(\"pwd\");")
    print("if (x.type === \"password\") {")
    print("x.type = \"text\";")
    print("} else {")
    print("x.type = \"password\";")
    print("}")
    print("}")
    print("</script>")


    print("""<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/
            3.6.1/jquery.min.js\"></script>""")


    print("<script>")
    print("$(document).ready(function(){")
    print("$(\"#submit_btn\").click(function(){")
    print("var form = $(\"#signup_form\");")
    print("$.ajax(")
    print("{")
    print("url: \"signup_auth.py\",")
    print("type: \"POST\",")
    print("data: form.serialize(),")
    print("success: function(result){")
    print("console.log(result.trim());")
    print("result = JSON.parse(JSON.stringify(result));")
    print("$(\"#div1\").html(result[\"a\"]);")
    print("},")
    print("error: function(result){")
    print("console.log(data)")
    print("}")
    print("}")
    print(");")
    print("});")
    print("});")
    print("</script>")

    print("</head>")
    return ""

def webpage_body_start():
    """ webpage_body_start """
    return "<body>"

def webpage_body():
    """ webpage_body """
    print("<div class=\"container border border-secondary rounded float-justify mt-4 \" ")
    print("<div class=\"card\" style=\"width:500px\" >")
    print("""<div class=\"card-header \" align=\"center\" >&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
        &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
        &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp    Sign Up   
        &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
        &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp 
        <a href=\"login.py\"> Login </a> 
        <p> Please fill in this form to create an account. </p> </div>""")

    print("""<form id=\"signup_form\" action=\"signup_auth.py\"
            method=\"POST\" class=\"card-body\" >""")
    print("<div class=\"form-group\">")
    print("<label for=\"email\">Email / Name:</label>")
    print("""<input type=\"email\" class=\"form-control\"
            id=\"email\" placeholder=\"Enter email / name\" name=\"email\" required >""")
    print("</div>")
    print("<div class=\"form-group\">")
    print("<label for=\"pwd\">Password:</label>")
    print("""<input type=\"password\" class=\"form-control\"
            id=\"pwd\" placeholder=\"Enter password\" name=\"pswd\" required >""")
    print("<input type=\"checkbox\" onclick=\"myFunction()\">Show Password")
    print("</div>")
    print("<div class=\"form-group\">")
    print("<label for=\"psw_repeat\">Repeat Password:</label>")
    print("""<input type=\"password\" class=\"form-control\"
            id=\"psw_repeat\" placeholder=\"Repeat Password\" name=\"psw_repeat\" required >""")
    print("</div>")
    print("<div class=\"form-group form-check\">")
    print("<label class=\"form-check-label\">")
    print("<input class=\"form-check-input\" type=\"checkbox\" name=\"remember\"> Remember me")
    print("</label>")
    print("</div>")
    print("<div class=\"form-group\" align=\"center\" >")
    print("""<button type=\"submit\" id=\"submit_btn\"
        class=\"btn btn-primary\">Submit</button>""")
    print("""<button type=\"button\" class=\"btn btn-danger\">
            <a href=\"http://localhost:8080/cgi-bin/home/home.py\"> Cancel </a> </button>""")
    print("</form>")

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
