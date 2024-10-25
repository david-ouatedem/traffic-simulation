import http.server
import socketserver
import json

PORT = 8080

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        # Parse incoming JSON data
        content_length = int(self.headers['Content-Length'])  # Get the length of the data
        post_data = self.rfile.read(content_length)  # Read the data
        json_data = json.loads(post_data)  # Parse JSON

        print("Received JSON data:")
        print(json.dumps(json_data, indent=4))  # Pretty-print the JSON

        # Send a response back to the client
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(b'{"status": "success"}')  # Respond with success message

# Start the server
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
