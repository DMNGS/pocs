import netman
import time
from umqttsimple import MQTTClient

# WiFi config
COUNTRY = '#ID#'
SSID = '#SSID#'
PASSWORD = '#PASSWORD#'

# MQTT config
BROKER = '#BROKER#'
ID_CLIENT = '#ID_CLIENT#'
A_USER = '#USER#'
A_PASSWORD = '#USER_PASS#'


class MQTTCon():
    def __init__(self):
        # Connect to WiFi
        self.wifi_connection = netman.connectWiFi(SSID,PASSWORD,COUNTRY)
        
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
        self.mqtt_connect()
