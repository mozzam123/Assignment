from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        response = {'message': 'Hello, this is a Python-made API!'}
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        response = {'message': f' Message: {data["message"]}'}
        print("Data from Post request:", response)
        self.wfile.write(json.dumps(response).encode())

def run(server_class=HTTPServer, handler_class=SimpleHandler, port=8888):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
