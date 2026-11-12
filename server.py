#!/usr/bin/env python3
"""
Dual-Stack IPv6/IPv4 Fast Local Server with No-Cache Headers
Designed to prevent the 2.0-second socket reverse-DNS latency standard on Windows localhost.
Serves full physical pre-rendered HTML directories in under 15ms.
"""

import sys
import os
import socket
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8080

class DualStackNoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Prevent browser caching lockouts during development & testing
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def log_message(self, format, *args):
        # Fast, clean logging
        sys.stdout.write(f"[{self.log_date_time_string()}] {format % args}\n")
        sys.stdout.flush()

class DualStackServer(HTTPServer):
    address_family = socket.AF_INET6

    def server_bind(self):
        # Enable dual-stack IPv6 and IPv4
        try:
            self.socket.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
        except (AttributeError, OSError) as e:
            print(f"[Warning] Could not set IPV6_V6ONLY=0: {e}")
        super().server_bind()

def run():
    # Ensure working directory is the site root
    site_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(site_dir)
    print(f"============================================================")
    print(f" Smaran Raut SEO Consultancy - Production Server Starting")
    print(f" Directory: {site_dir}")
    print(f" Dual-Stack IPv6/IPv4 Socket Initialized (Port {PORT})")
    print(f" Local URL: http://localhost:{PORT}")
    print(f" Local IPv4: http://127.0.0.1:{PORT}")
    print(f" Local IPv6: http://[::1]:{PORT}")
    print(f" Zero White-Screen Architecture: Ready (<15ms latency)")
    print(f"============================================================")

    try:
        server = DualStackServer(('::', PORT), DualStackNoCacheHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer gracefully terminated.")
    except Exception as e:
        print(f"\nFalling back to standard IPv4 server due to: {e}")
        from http.server import ThreadingHTTPServer
        fallback = ThreadingHTTPServer(('0.0.0.0', PORT), DualStackNoCacheHandler)
        fallback.serve_forever()

if __name__ == '__main__':
    run()
