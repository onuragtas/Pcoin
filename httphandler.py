from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import sqlite3
class httphandler(BaseHTTPRequestHandler):
    

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        conn = sqlite3.connect('pcoin.db')
        c = conn.cursor()
        path = self.path.replace("/","")
        self._set_headers()
        self.wfile.write("<html><head><meta http-equiv=\"refresh\" content=\"30\"></head><body><table><thead><th>#</th><th>Process</th><th>Coin</th><th>Value</th><th>Amount</th></thead><tbody>")
        if path == "":
            read = conn.cursor().execute("SELECT * FROM process").fetchall()
        else:
            read = conn.cursor().execute("SELECT * FROM process WHERE coin='"+path+"'").fetchall()
        for item in read:
            self.wfile.write("<tr><td>"+str(item[0])+"</td><td>"+str(item[1])+"</td><td>"+str(item[2])+"</td><td>"+str(item[3])+"</td><td>"+str(item[4])+"</td></tr>")
        self.wfile.write("</tbody></table></body></html>")
        c.close()
        conn.close()

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")