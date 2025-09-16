import http.server as BaseHTTPServer


class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    '''Handle HTTP requests by returning a fixed 'page'.'''

    # Page to send back
    Page = '''\
<html>
<body>
<p>Hello Word, Web</p>
</body>
</html>
'''

    # Handle get request
    def do_GET(self):
        body = self.Page.encode('utf-8')
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.send_header("content-length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()