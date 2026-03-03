#!/usr/bin/env python3
"""
Servidor para Neon Snake
Ejecuta: python server.py
Luego abre: http://localhost:8080
"""

import http.server
import socketserver
import os
import webbrowser
import threading

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        # Mensajes de acceso limpios
        print(f"  [{self.address_string()}] {format % args}")

def open_browser():
    import time
    time.sleep(0.8)
    webbrowser.open(f"http://localhost:{PORT}")

if __name__ == "__main__":
    os.chdir(DIRECTORY)

    print("=" * 50)
    print("  🐍  NEON SNAKE - Servidor iniciado")
    print("=" * 50)
    print(f"  URL:   http://localhost:{PORT}")
    print(f"  Dir:   {DIRECTORY}")
    print("  Abriendo el navegador...")
    print("  Presiona Ctrl+C para detener")
    print("=" * 50)

    # Abrir navegador automáticamente
    threading.Thread(target=open_browser, daemon=True).start()

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.allow_reuse_address = True
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n  Servidor detenido. ¡Hasta luego!")
