'''Home Generator'''

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
    '''Webpage start'''
    return '<html>'

def webpage_head(title):
    '''Home page body start'''
    
    print('<head>')
    print('<meta name="viewport" content="width=device-width, initial-scale=1">')
    print(f"<title> {title} </title>")
    print('<style>')
    
    print('''
    ul {
		list-style-type: none;
		margin: 0;
		padding: 0;
		overflow: hidden;
		background-color: #333;
	   }

	li {
		float: left;
	}

	li a {
		display: block;
		color: white;
		text-align: center;
		padding: 14px 16px;
		text-decoration: none;
	}

	li a:hover:not(.active) {
		background-color: #111;
	}

	.active {
		background-color: #04AA6D;
	}
	''')

    print('''
	* {
	box-sizing: border-box;
	}

	body {
	font-family: Arial, Helvetica, sans-serif;
	}

	/* Float three columns side by side */
	.column {
	float: left;
	width: 33.3%;
	padding: 30px 30px;
	}

	/* Remove extra left and right margins, due to padding */
	.row {margin: 0 -5px;}

	/* Clear floats after the columns */
	.row:after {
	content: "";
	display: table;
	clear: both;
	}

	/* Responsive columns */
	@media screen and (max-width: 1000px) {
	.column {
		width: 50%;
		display: block;
		margin-bottom: 20px;
	}
	}

	@media screen and (max-width: 600px) {
	.column {
		width: 100%;
		display: block;
		margin-bottom: 20px;
	}
	}

	/* Style the counter cards */
	.card {
	box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
	padding: 12px;
	text-align: center;
	background-color: #f1f1f1;
	transition: 0.3s;
	border-radius: 10px;
	}

	.card:hover {
	box-shadow: 0 4px 30px 0 rgba(0,0,0,0.4);
	}

	img {
	border-radius: 10px 10px 10px 10px;
	}
	''')

    print("</style>")
    print("</head>")
    return ''

def webpage_body_start():
    """webpage_body_start"""
    return "<body>"

def webpage_body():
    '''Home page body'''

    print('''
    <ul>
    <li><a href=\"http://localhost:8080/cgi-bin/home/home.py\">Home</a></li>
    <li><a href=\"http://localhost:8080/cgi-bin/home/home_contact.py\">Contact</a></li>
    <li><a href=\"http://localhost:8080/cgi-bin/home/home_about.py\">About</a></li>
    <li style="float:right"><a class="active" href=\"http://localhost:8080/cgi-bin/login/login.py\">Login</a></li>
    <li style="float:right"><a class="active" href=\"http://localhost:8080/cgi-bin/login/signup.py\">Sign Up</a></li>
    </ul>
    ''')

    data = employee_data()
    for elements in data:

        print("<div class=\"column\">")
        print("<div class=\"row\">")
        print("<div class=\"card\">")

        print(f"<h3 class=\"card-title\">{elements[1]}</h3>")
        print(f"<p class=\"card-text\">Employee ID : {elements[0]}</p>")
        print(f"<p class=\"card-text\"> Phone : {elements[2]}</p>")
        print(f"<p class=\"card-text\"> Location : {elements[3]}</p>")
        
        print('''
		<div class="button-container">
		<button class="button"> <a class="button" href=\"http://localhost:8080/cgi-bin/home/home_employee_edit.py\"> Edit </a></button>
		<button class="button">	<a class="button" href=\"http://localhost:8080/cgi-bin/home/home_employee_edit.py\"> Delete </a></button>
		</div>
    ''')

        print("<br>")
        print("</div>")
        print("</div>")
        print("</div>")
    return ''

def webpage_body_end():
    '''Home page body end'''
    return '</body>'

def webpage_end():
    '''Webpage End'''
    return '</html>'
