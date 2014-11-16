import os
import BaseHTTPServer
import urlparse
import cgi
import shutil

PORT = int(os.getenv("VCAP_APP_PORT", "8000"))

class IEOHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_error(404)
    def do_GET(self):
        parsed = urlparse.urlparse(self.path)

        if parsed.path != "/retrieve" and parsed.path != "/output.jpg" and parsed.path != "/outputprice.jpg":
            self.send_error(404)
            return

        self.send_response(200)

        if parsed.path == "/output.jpg":
            self.send_header("Content-type", "image/jpeg")
            self.end_headers()
            with open("output.jpg", "r") as f:
                shutil.copyfileobj(f, self.wfile)
            return
        if parsed.path == "/outputprice.jpg":
            self.send_header("Content-type", "image/jpeg")
            self.end_headers()
            with open("outputprice.jpg", "r") as f:
                shutil.copyfileobj(f, self.wfile)
            return


        import retrieve
        out = retrieve.handleRetrieve(cgi.parse_qs(parsed.query), self)

        self.send_header("Content-type", out[0])
        self.end_headers()

        self.wfile.write(bytes(out[1], "UTF-8"))

httpd = BaseHTTPServer.HTTPServer(("", PORT), IEOHandler)
print("Starting at port", PORT)
httpd.serve_forever()