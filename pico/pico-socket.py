import network
import socket
import time

import machine

potent = machine.ADC(26)

SSID = 'Tech2'
PASSWORD = 'Super2012'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

html = """<!DOCTYPE html5>
<html>
    <head><title>Pico W</title></head>
    <body>
        <h1>Pico W</h1>
        <p>Hello World!</p>
    </body>
</html>
"""

# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('connecting...')
    time.sleep(1)
    
# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('Network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print(f'ip = {status[0]}')
    
# Open socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

# Listen for connections
while True:
    try:
        cl, addr = s.accept()
        print('client connected form', addr)
        cl_file = cl.makefile('rwb', 0)
        while True:
            line = cl_file.readline()
            if not line or line == b'\r\n':
                break
        
        response = html + str(potent.read_u16())
        cl.send('HTTP/1.0 200 OK \r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
        
    except OSError as e:
        cl.close()
        print('connection closed')