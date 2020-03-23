import time
from http.server import BaseHTTPRequestHandler,HTTPServer
import PoeChaosRecipe


HOST_NAME = ''
PORT_NUMBER = 820


class PoeHttpHander(BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        if s.path != "/chaos":
            print("path not found: "+s.path)
            s.send_response(404)
            return
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><title>Chaos recipe status</title></head>".encode())
        s.wfile.write("<body><h1>Chaos recipe status</h1>".encode())
        printChaosAmounts(s.wfile, getChaosItems())
        s.wfile.write("</body></html>".encode())

def startWebServer():
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), PoeHttpHander)
    print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))

def getChaosItems():
    return PoeChaosRecipe.getTabContents()

def printChaosAmounts(wfile, chaosItems):
    wfile.write(("<br/>helmets: "+str(PoeChaosRecipe.countChaosItem(chaosItems, 'isHelmet'))).encode())
    wfile.write(("<br/>gloves: " + str(PoeChaosRecipe.countChaosItem(chaosItems, 'isGloves'))).encode())
    wfile.write(("<br/>boots: " + str(PoeChaosRecipe.countChaosItem(chaosItems, 'isBoots'))).encode())
    wfile.write(("<br/>rings: " + str(PoeChaosRecipe.countChaosItem(chaosItems, 'isRing'))).encode())
    wfile.write(("<br/>amulets: " + str(PoeChaosRecipe.countChaosItem(chaosItems, 'isAmulet'))).encode())
    wfile.write(("<br/>belts: " + str(PoeChaosRecipe.countChaosItem(chaosItems, 'isBelt'))).encode())
    wfile.write(("<br/>weapons: " + str(PoeChaosRecipe.countChaosItem(chaosItems, 'isChaosWeapon'))).encode())
    wfile.write(("<br/>body: " + str(PoeChaosRecipe.countChaosItem(chaosItems, 'isBodyArmour'))).encode())