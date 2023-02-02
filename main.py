"""
	main file to start the application
"""

# https://pointlessprogramming.wordpress.com/2011/02/13/python-cgi-tutorial-1/
# https://docs.python.org/3/library/http.server.html

import socket
import http.server
import webbrowser
import sys


PORT = 8080


def port_check(host):
    """
            return True if the port is available else False
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)  # Timeout in case of port not open
    try:
        sock.connect_ex((host, PORT))
        sock.close()
        return True
    except Exception as exc:  # pylint: disable=W0718
        print(exc)
        return False


if not port_check("localhost"):
    print(f"Port {PORT} is not available...")
    sys.exit(0)


SCRIPT_PATH = "cgi-bin/login/login.py"

Serverclass = http.server.HTTPServer
Handlerclass = http.server.CGIHTTPRequestHandler
server_address = ("", PORT)

httpd = Serverclass(server_address, Handlerclass)

URL = f'http://localhost:{PORT}/{SCRIPT_PATH}'

webbrowser.open_new_tab(URL)

print("serving at", URL)
print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()
