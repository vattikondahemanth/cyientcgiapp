''' Login base page generator'''
import cgitb

try:
    from home_profile import employee_data  # pylint: disable=E0401
    
except ModuleNotFoundError:
	import os
	import sys ;
        
	sys.path.append(os.getcwd() + '\\cgi-bin\\')
	from home.home_profile import employee_data

cgitb.enable()

def cgi_content(re_type="text/html"):
    '''Cgi content'''
    return 'Content type: ' + re_type

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

    print("""<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/
            3.6.1/jquery.min.js\"></script>""")


    print("<script>")
    print("$(document).ready(function(){")
    print("$(\"#submit_btn\").click(function(){")
    print("var form = $(\"#edit_info_form\");")
    print("$.ajax(")
    print("{")
    print("url: \"edit_info_auth.py\",")
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


def webpage_edit_body(data):
    """ webpage_edit_body """
    print("<div class=\"container border border-secondary rounded float-justify mt-4 \" ")
    print("<div class=\"card\" style=\"width:500px\" >")
    print("""<div class=\"card-header \" align=\"center\" >Edit Info</div>""")

    print("<form id=\"edit_info_form\" action=\"edit_info_auth.py\" method=\"POST\"  class=\"card-body\" >")
    
    print("<div class=\"form-group\">")
    print("<label for=\"email\">Email / Name :</label>")
    print(f"""<input type=\"email\" class=\"form-control\" value={data[0][1]}  readonly
            id=\"email\" placeholder=\"Enter email / name\" name=\"email\" required >""")
    print("</div>")

    print("<div class=\"form-group\">")
    print("<label for=\"emp_id\">Employee ID :</label>")
    print(f"""<input type=\"text\" class=\"form-control\" value={data[0][0]}
            id=\"emp_id\" placeholder=\"Enter Employee ID\" name=\"emp_id\" required >""")
    print("</div>")

    print("<div class=\"form-group\">")
    print("<label for=\"number\">Phone Number :</label>")
    print(f"""<input type=\"ph_num\" class=\"form-control\" value={data[0][2]}
            id=\"ph_num\" placeholder=\"Enter Phone Number\" name=\"ph_num\" >""")
    print("</div>")
    address_var = data[0][3]
    print("<div class=\"form-group\">")
    print("<label for=\"text\">Addres :</label>")
    print(f"""<input type=\"address\" class=\"form-control\" value={address_var}
            id=\"address\" placeholder=\"Enter Addres\" name=\"address\" >""")
    print("</div>")

    print("<div  class=\"form-group\" align=\"center\" >")
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

def response(data):
    """ response """
    message = data["message"]
    print("<div class=\"alert alert-danger\">")
    print(f"<h6 align=\"center\" > <strong>{message}</strong> </h6>")
    print("</div>")
    return ""


def webpage_body_end():
    """ webpage_body_end """
    return "</body>"

def webpage_end():
    """ webpage_end """
    return "</html>"
