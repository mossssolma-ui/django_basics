import os
from http.server import BaseHTTPRequestHandler

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов
    """

    def do_GET(self) -> None:
        """Метод для обработки входящих GET-запросов"""
        try:
            if self.path.startswith("/static/"):
                file_path = os.path.join("src", "web_app", "site_html", self.path[1:])
                ext = self.path.split(".")[-1]
                content_type = {
                    "css": "text/css",
                    "js": "application/javascript",
                    "png": "image/png",
                    "svg": "image/svg+xml",
                    "jpg": "image/jpeg",
                    "jpeg": "image/jpeg",
                }.get(ext, "application/octet-stream")
                print(f"Static: {self.path}")
            else:
                file_path = os.path.join("src", "web_app", "site_html", "contact.html")
                content_type = "text/html"
                print(f"GET {self.path} -> contact.html")

            with open(file_path, "rb") as f:
                self.send_response(200)
                self.send_header("Content-type", content_type)
                self.end_headers()
                self.wfile.write(f.read())

        except FileNotFoundError:
            self.send_error(404)
