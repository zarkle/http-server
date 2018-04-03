from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
from cowpy import cow


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        if parsed_path.path == '/':
            self.send_response(200)
            self.end_headers()

            self.wfile.write(b"""<!DOCTYPE html>
<html>
<head>
    <title> cowsay </title>
</head>
<body>
    <header>
        <nav>
        <ul>
            <li><a href="/cowsay">cowsay</a></li>
        </ul>
        </nav>
    <header>
    <main>
        <p>cowsay is a program that generates ASCII pictures of a cow with a message. This is my first time making an HTTP server in Python</p>
    </main>
</body>
</html>""")
            return

        elif parsed_path.path == '/cowsay':
            self.send_response(200)
            self.end_headers()

            self.wfile.write(b"""<!DOCTYPE html>
<html>
<head>
    <title> cowsay </title>
</head>
<body>
    <header>
        <nav>
        <ul>
            <li><a href="/">Home</a></li>
        </ul>
        </nav>
    <header>
    <main>
        <p>A message about other things you can do</p>
    </main>
</body>
</html>""")


        elif parsed_path.path == '/cow?msg=my+message':
            try:
                cat = json.loads(parsed_qs['category'][0])
            except KeyError:
                self.send_response(400)
                self.end_headers
                self.wfile.write(b'You did a bad thing')
                return

            self.send_response(200)
            self.end_headers
            self.wfile.write(b'We did the thing with the qs')
            return

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

    def do_POST(self):
        parse_qs


def create_server():
    return HTTPServer(('127.0.0.1', 3000), SimpleHTTPRequestHandler)


def run_forever():
    server = create_server()

    try:
        print('Starting server on port 3000')
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()


if __name__ == '__main__':
    run_forever()
