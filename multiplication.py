from http.server import HTTPServer, BaseHTTPRequestHandler

content="""
<!DOCTYPE html>
<html>
<head><title>WEBSERVER</title>
</head>
<body>
<h1 style="color:purple;text-align:center;font-family:castellar;font-size:60px";>11 TIMES TABLE</h1>
<hr size="2" width="100%" color="blue">

<p style="text-align:center;font-size:40px;font-family:berlin sans FB";>11 X 0 = 0</p>
<p style="text-align:center;font-size:40px;font-family:berlin sans FB";>11 X 1 = 11</p>
<p style="text-align:center;font-size:40px;font-family:berlin sans FB";>11 X 2 = 22</p>
<p style="text-align:center;font-size:40px;font-family:berlin sans FB";>11 X 3 = 33</p>
<p style="text-align:center;font-size:40px;font-family:berlin sans FB";>11 X 4 = 44</p>
<p style="text-align:center;font-size:40px;font-family:berlin sans FB";>11 X 5 = 55</p>
<p style="text-align:center;font-size:40px;font-family:berlin sans FB";>11 X 6 = 66</p>
<p style="text-align:center;font-size:40px;font-family:berlin sans FB";>11 X 7 = 77</p>
<p style="text-align:center;font-size:40px;font-family:berlin sans FB";>11 X 8 = 88</p>
<p style="text-align:center;font-size:40px;font-family:berlin sans FB";>11 X 9 = 99</p>
<p style="text-align:center;font-size:40px;font-family:berlin sans FB";>11 X 10 = 110</p>
</body>
</html>"""
class Mypage(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Request Received")
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

server_address=('',80)
httpd = HTTPServer(server_address,Mypage)
httpd.serve_forever()