from http.server import BaseHTTPRequestHandler, HTTPServer

class RedirectHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(302)  # Send redirect
        self.send_header('Location', self.path.split("url=")[-1])
        self.end_headers()

    def do_HEAD(self):
        """Handle HEAD requests like GET, but without a body"""
        self.send_response(302)
        self.send_header('Location', self.path.split("url=")[-1])
        self.end_headers()

if __name__ == '__main__':
    server_address = ('', 8000)  # Run on port 8000
    httpd = HTTPServer(server_address, RedirectHandler)
    print("Serving on port 8000...")
    httpd.serve_forever()
