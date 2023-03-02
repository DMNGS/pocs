import network
import time
import machine
from umqttsimple import MQTTClient # From https://github.com/RuiSantosdotme/ESP-MicroPython/blob/master/code/MQTT/umqttsimple.py

# WiFi config
SSID = '#SSID'
PASSWORD = '#PASSWORD'

# MQTT config
BROKER = '#BROKER'
ID_CLIENT = 'PicoW'
A_USER = '#USER'
A_PASSWORD = '#PASSWORD'

def connectWiFi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    # Wait for connect or fail
    max_wait = 10
    while max_wait > 0:
        if wlan.status() < network.STAT_IDLE or wlan.network.STAT_GOT_IP:
            break
        max_wait -= 1
        print('waiting for connection...')
        time.sleep(1)

    # Handle connection error
    if wlan.status() != network.STAT_GOT_IP:
        raise RuntimeError('network connection failed')
    else:
        print('connected')
        status = wlan.ifconfig()
        print( 'ip = ' + status[0] )
    return status

class MQTTCon():
    def __init__(self):
        # Connect to WiFi
        self.wifi_connection = connectWiFi()
        
        self.mqtt_connect()
        
    # Send message to broker
    def send_msg(self, message, topic):
        try:
            self.client.publish(topic, msg=message)
            print('published')
        except:
            self.reconnect()
            pass

    # MQTT connect
    def mqtt_connect(self):
        print('Connecting to broker')
        try:
            self.client = MQTTClient(ID_CLIENT, BROKER, user=A_USER, password=A_PASSWORD, keepalive=60)
            self.client.connect()
            print(f'Connected to {BROKER} MQTT Broker')
        except OSError as e:
            self.reconnect()

    # Reconnect & Reset
    def reconnect(self):
        print('Failed to connected to MQTT Broker. Reconnecting...')
        time.sleep(5)
        machine.reset()

