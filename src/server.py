from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
from cowpy import cow


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """request handler"""
    def do_GET(self):
        """handle GET routes"""
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
        <p>A message about other things you can do. After the port number, add <b>cow?msg="message"</b> in the address bar, replacing message with your message </p>
    </main>
</body>
</html>""")
            return

        elif parsed_path.path == '/cow':
            try:
                daemon = cow.Daemon()
                msg = daemon.milk(json.loads(parsed_qs['msg'][0]))
            except (KeyError, json.decoder.JSONDecodeError):
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'Incorrect format')
                return

            self.send_response(200)
            self.end_headers()
            self.wfile.write(msg.encode('utf8'))
            return

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

    def do_POST(self):
        """handle POST routes"""
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        if parsed_path.path == '/cow':
            try:
                daemon = cow.Daemon()
                msg = daemon.milk(json.dumps(parsed_qs['msg'][0]))
                post_dict = {'content': msg}
            except (KeyError, json.decoder.JSONDecodeError):
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'Incorrect format')
                return

            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(post_dict).encode('utf8'))
            return

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')


def create_server():
    """create server"""
    return HTTPServer(('127.0.0.1', 3000), SimpleHTTPRequestHandler)


def run_forever():
    """keep server running forever"""
    server = create_server()

    try:
        print('Starting server on port 3000')
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()


if __name__ == '__main__':
    run_forever()
