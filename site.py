import http.server
import socketserver
import os
import hashlib

# CONFIGURAÇÕES TÁTICAS
PORT = 8080
DIRECTORY = "."

class BarbieriHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, *args, **kwargs)

def check_integrity():
    """Gera um hash simples do index.html para monitorar alterações"""
    if os.path.exists("index.html"):
        with open("index.html", "rb") as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()
            print(f"[LOG] Integridade index.html: {file_hash[:15]}...")
            return file_hash
    return None

def start_server():
    """Inicia o servidor de testes da Barbieri Security RD"""
    try:
        with socketserver.TCPServer(("", PORT), BarbieriHandler) as httpd:
            print(f"\n[SISTEMA ATIVO] Servidor rodando em: http://localhost:{PORT}")
            print(f"[INFO] Pressione CTRL+C para encerrar o deploy.")
            check_integrity()
            httpd.serve_forever()
    except Exception as e:
        print(f"[ERRO] Falha ao iniciar servidor: {e}")

if __name__ == "__main__":
    start_server()