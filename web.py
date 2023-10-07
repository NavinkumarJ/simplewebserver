from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title>My webserver</title>
</head>

<body bgcolor="pink">
<h1>Top 5 E-Shopping Companies!<h1>
<ol aling='center'>
<li>Amazon</li>
<li>Flipkart</li>
<li>Meesho</li>
<li>e-bay</li>
<li>shopsy</li>
</ol>
</body>

</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()