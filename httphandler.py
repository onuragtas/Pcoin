#-*-coding:utf-8 -*-
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
        if path == " ":
            read = conn.cursor().execute("SELECT * FROM process").fetchall()
        elif path == "datas":
            read = conn.cursor().execute("SELECT * FROM datas GROUP BY coin").fetchall()
            self.wfile.write("<html><head><title>Değerler</title></head><body><table><thead><th>#</th><th>Coin</th><th>Value</th></thead><tbody>")
            i = 1
            for item in read:
                self.wfile.write("<tr><td>"+str(i)+"</td><td><a href=\"/values/"+str(item[1])+"\">"+str(item[1])+"</a></td><td>"+str(item[2])+"</td></tr>")
                i = i + 1
            self.wfile.write("</tbody></table></body></html>")
        elif path.find("values")!=-1:
            read = conn.cursor().execute("SELECT * FROM datas WHERE coin='"+path.replace("values","")+"'").fetchall()
            self.wfile.write("<html><head><title>Değerler</title></head><body><table><thead><th>#</th><th>Coin</th><th>Value</th></thead><tbody>")
            for item in read:
                self.wfile.write("<tr><td>"+str(item[0])+"</td><td>"+str(item[1])+"</td><td>"+str(item[2])+"</td></tr>")
            self.wfile.write("</tbody></table></body></html>")
        else:
            read = conn.cursor().execute("SELECT * FROM process WHERE coin='"+path+"'").fetchall()
            self.wfile.write("<html><head><title>"+ str(len(read)) +"</title><meta http-equiv=\"refresh\" content=\"30\"></head><body><table><thead><th>#</th><th>Process</th><th>Coin</th><th>Value</th><th>Amount</th></thead><tbody>")
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