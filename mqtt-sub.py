from paho.mqtt import client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print('Connected to MQTT Broker!')
    else:
        print('Failed to connect, return code %d\n', rc)


def on_message(client, userdata, message):
    print('recived message: ', str(message.payload.decode('utf-8')))
    
mqttBroker = 'sdmansion.local'

client = mqtt.Client('Server')
client.username_pw_set(username='buffet', password='tastybuffet')
client.on_connect = on_connect
client.on_message = on_message

client.connect(mqttBroker)

client.loop_start()

client.subscribe('scale/value')

try:
    while True:
        pass
except:
    print('Stopping')
    client.loop_stop()