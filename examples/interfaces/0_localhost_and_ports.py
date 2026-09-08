"""Before any interface: what localhost and a port actually are.

Run it:  python 0_localhost_and_ports.py
Stop it: Ctrl+C

Then open the address it prints. You have just used the same machinery as every
website you visit, with nine lines of Python and no library.

The vocabulary, in one paragraph
--------------------------------
TCP/IP is the postal system of a network. To deliver anything you need an
address, which says WHICH MACHINE, and a port, which says WHICH DOOR on that
machine. 127.0.0.1, also written localhost, is a special address meaning "this
machine, right here". A port is just a number: one program per door.

So http://127.0.0.1:8000 reads: this machine, door 8000, speak the language of
the web. Nobody outside can knock on that door. That is the whole difference
between running something and publishing it.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer

ADDRESS = "127.0.0.1"    # this machine, and only this machine
PORT = 8000              # the door. Change it to 8001 and the address changes too


class Page(BaseHTTPRequestHandler):
    def do_GET(self):
        """Called every time a browser knocks on the door."""
        self.send_response(200)                     # 200 means: here you go
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        # A browser expects bytes, not text, so encode() converts it
        html = "<h1>It works</h1><p>Served by your own Python, on port %d.</p>" % PORT
        self.wfile.write(html.encode("utf-8"))

    def log_message(self, *args):
        """Silence the default logging so the terminal stays readable."""
        return


def main():
    server = HTTPServer((ADDRESS, PORT), Page)
    print("Open this address in a browser:")
    print("    http://%s:%d" % (ADDRESS, PORT))
    print("In a Codespace, click the notification that offers to open the port.")
    print("Ctrl+C to stop.")
    server.serve_forever()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nServer stopped. The door is closed again.")

# What to remember
# 1. An address says which machine, a port says which door. That is TCP/IP
# 2. 127.0.0.1, or localhost, means this machine. Nobody else can reach it
# 3. Gradio uses port 7860, Streamlit uses 8501. Same idea, same address
# 4. Running something and publishing it are two different things
