from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b"Hello from Effective Mobile!\n")
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    server_address = ('', 8080)
    print("Starting backend server on port 8080")
    httpd = HTTPServer(server_address, SimpleHandler)
    httpd.serve_forever()