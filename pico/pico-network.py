import network
import time

import machine

potent = machine.ADC(26)

SSID = 'Tech2'
PASSWORD = 'Super2012'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < network.STAT_IDLE or wlan.status() >= network.STAT_GOT_IP:
        break
    max_wait -= 1
    print('connecting...')
    time.sleep(1)
    
# Handle connection error
if wlan.status() != network.STAT_GOT_IP:
    raise RuntimeError('Network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print(f'ip = {status[0]}')