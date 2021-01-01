from http.server import BaseHTTPRequestHandler, HTTPServer
class HandleRequests(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(b"received get request!")
    
    def do_POST(self):
        self._set_headers()
        content_len = int(self.headers.getheader('content-lengt',0))
        post_body = self.rfile.read(content_len)
        self.wfile.write(b"Received post request:{}".format(post_body))

    def do_PUT(self):
        self.do_POST()

host = ''
port = 8080
HTTPServer((host,port), HandleRequests).serve_forever()
