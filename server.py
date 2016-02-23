# import http.server
# import socketserver

# The following listens on port 8000
# PORT = 8000
# Handler = http.server.SimpleHTTPRequestHandler
# httpd = socketserver.TCPServer(("", PORT), Handler)
#
# print("Serving at port", PORT)
# httpd.serve_forever()


import time
import BaseHTTPServer
import urlparse
import os
import pickle

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        print(self.address_string())
        self.end_headers()
        currentPath = os.getcwd() + "/pressure.txt"

        f = open(currentPath)
        self.wfile.write(f.read())
        f.close()

        os.system("rm double_wedge.txt pressure.txt")
        # s.wfile.write("<html><head><title>Title goes here.</title></head>")
        # s.wfile.write("<body><p>This is a test.</p>")
        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".
        #       s.wfile.write("<p>You accessed path: %s</p>" % s.path)
        #       s.wfile.write("</body></html>")
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        post_data = self.rfile.readline(int(self.headers.getheader('Content-Length')))
        post_data = urlparse.parse_qs(post_data)
        output = open('inputFile.txt', 'w')
        pickle.dump(post_data, output)
        output.close()
        os.system("python callSolver.py")

HOST_NAME = 'wolverine.cs.wright.edu'
PORT_NUMBER = 8000
server_class = BaseHTTPServer.HTTPServer
httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
httpd.serve_forever()
