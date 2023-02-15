''' Login base page generator'''

def cgi_content(re_type="text/html"):
    """ cgi_content """
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
    print("$(\"#delete_btn\").click(function(){")
    print("var form = $(\"#delete_form\");")
    print("$.ajax(")
    print("{")
    print("url: \"delete_info_auth.py\",")
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

def webpage_body(username):
    """ webpage_body """
    print("<div class=\"container border border-secondary rounded float-justify mt-4 \" ")
    print("<div class=\"card\">")

    print("<form id=\"delete_form\" action=\"delete_info_auth.py\" method=\"POST\"  class=\"card-body\" >")

    print("<div class=\"form-group\">")
    print(f"""<input type=\"hidden\" id=\"username\" value=\"{username}\" name=\"username\">""")
    print(f"<h1 align=\"center\"> {username} </h1>")
    print(f"<p align=\"center\"> Are you sure you want to delete <strong> {username} </strong> </p>")
    print("</div>")

    print("<div  class=\"form-group\" align=\"center\" >")
    print("""<button type=\"submit\" id=\"delete_btn\"
    class=\"btn btn-primary\">Submit</button>""")
    print("""<button type=\"button\" class=\"btn btn-danger\">
            <a href=\"http://localhost:8080/cgi-bin/home/home.py\"> Cancel </a> </button>""")
    print("</div>")
    print("</form>")
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
