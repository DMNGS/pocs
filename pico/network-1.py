import network
import ubinascii
import time
import urequests

SSID = 'Tech2'
PASSWORD = 'Super2012'

wlan = network.WLAN(network.STA_IF)
rp2.country('CH')
wlan.active(True)
wlan.connect(SSID, PASSWORD)

def socket_http():
    import socket
    # Get IP address for google.com
    ai = socket.getaddrinfo('google.com', 80)
    addr = ai[0][-1]
    
    # Create a socket and make a HTTP request
    s = socket.socket()
    s.connect(addr)
    s.send(b"GET / HTTP/1.0\r\n\r\n")
    
    # Print the response
    print(s.recv(512))
    
def urequest_http():
    r = urequests.get("http://www.google.com")
    print(r.content)
    r.close()

# Wait for connect to fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)
    
# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    mac = ubinascii.hexlify(network.WLAN().config('mac'), ':').decode()
    print(mac)
    
    urequest_http()