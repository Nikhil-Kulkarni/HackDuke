import os
import http.server
import socketserver
import urllib

PORT = int(os.getenv("VCAP_APP_PORT", "8000"))

class DietrHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        path = urllib.parse.urlparse(self.path).path

        postvars = self.rfile.read(int(self.headers["Content-Length"]))

        if path != "/login" and path != "/register" and path != "/retrieve":
            self.send_error(404)
            return

        self.send_response(200)

        if path == "/login":
            import login
            out = login.handleLogin(postvars, self)
        elif path == "/register":
            import register
            out = register.handleRegister(postvars)
        elif path == "/retrieve":
            import retrieve
            out = retrieve.handleRetrieve(postvars, self)

        self.send_header("Content-type", out[0])
        self.end_headers()

        self.wfile.write(bytes(out[1], "UTF-8"))
    def do_GET(self):
        self.send_error(404)

httpd = socketserver.TCPServer(("", PORT), DietrHandler)
print("Starting at port", PORT)
httpd.serve_forever()