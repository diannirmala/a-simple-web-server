"""
simple_http_server.py

HTTP server sederhana (Python 3)
- Listen di port 8080
- Handle HTTP GET
- Return HTML statis
"""

from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    '''Handle HTTP requests by returning a fixed 'page'.'''

    # Page to send back.
    Page = '''\
<html>
<body>
<p>Hello, web!</p>
</body>
</html>
'''

    # Handle a GET request.
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(self.Page)))
        self.send_header("Connection", "close")
        self.end_headers()
        self.wfile.write(self.Page)

#----------------------------------------------------------------------

if __name__ == '__main__':
    serverAddress = ('', 8000)
    server = HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()

"""
## Known Issues / Environment Notes

### Windows Firewall

When running the HTTP server on Windows, the server may appear to load slowly
or connections may hang if `python.exe` is blocked by Windows Defender Firewall.

This can occur if firewall access is declined when first running the server.

Symptoms:
- Browser keeps loading
- Server prints "Serving on port XXXX..." but no response is shown

Cause:
- Incoming connections to the Python process are blocked by the OS firewall

Resolution:
- Allow Python through Windows Defender Firewall on private networks
- Or document this behavior when firewall access is intentionally declined

"""