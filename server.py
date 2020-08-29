from http.server import HTTPServer, BaseHTTPRequestHandler as BH
from urls import allUrls, http_404

class Server(BH):
    
    def do_GET(self):
        
        def error_404():
            html = open(http_404).read()
            self.send_response(400)
                
            self.end_headers()
            self.wfile.write(bytes(html, "utf-8"))
            return
        
        self.templatename = None
    
        for url in allUrls:
            if self.path == url:
                self.templatename = allUrls[url]
                
        if self.templatename:
            html = open(self.templatename).read()
            self.send_response(200)
                
            self.end_headers()
            self.wfile.write(bytes(html, "utf-8"))
        else:
            error_404()

with HTTPServer(("127.0.0.1", 8080), Server) as httpd:
    print("--> http://127.0.0.1:8080")
    print("Running...")
    httpd.serve_forever()
                