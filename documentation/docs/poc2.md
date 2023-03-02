# PoC 2: Connécter un Raspberry Pi Pico à un serveur MQTT et y envoyer des données

Le but de ce PoC est de prendre le code fait pour [le premier](./poc1.md) et d'y ajouté la connectivité vers un broker MQTT

## Se connecter au réseau
Avant de pourvoir se connecter au broker, il faut se connecter au même réseau que lui. Pour ça il faut utiliser la librairie `network`. On crée une instance de network.WLAN en mode station/client(STA_IF) puis on appèle la fonction `connect()` pour se connecter. On peut s'arrêter là, mais il est bon de vérifier que la connexion à réussi. La méthode la plus commune (et celle donnée par la documentation) est de vérifier un nombre de fois le status de la connection et de s'arrèter soit quand le nombre d'essais est dépassé ou quand le status indique qu'il n'est ni en attente ni en connexion. Puis, de vérifier que le status indique que la connexion a réussi.

```python title="Un fonction de connexion"
import network

def connectWiFi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect('WiFiMaison', 'legosseprefere')
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
```

## Connexion au broker et envoie des données
Une fois connecté au réseau, on se connecte au broker. Encore une fois une librairie est utilisée, dans ce cas la librairie [umqttsimple](https://github.com/RuiSantosdotme/ESP-MicroPython/blob/master/code/MQTT/umqttsimple.py) par Rui Santos.

Pour la connexion, on doit donner un ID client, l'addresse du broker, le nom d'utilisateur, le mot de passe et le temps de vie sur le broker.

```python title="Connexion MQTT"
import time
import machine
from umqttsimple import MQTTClient

def mqtt_connect():
        print('Connecting to broker')
        try:
            client = MQTTClient(ID_CLIENT, BROKER, user=A_USER, password=A_PASSWORD, keepalive=60)
            client.connect()
            print(f'Connected to {BROKER} MQTT Broker')
        except OSError as e:
            reconnect()

# Reconnect & Reset
    def reconnect():
        print('Failed to connected to MQTT Broker. Reconnecting...')
        time.sleep(5)
        machine.reset()
```

Ensuite, pour envoyer des données on indique le message et le topic dans lequel l'envoyer.

```python title="Envoie de message"
# Send message to broker
    def send_msg(topic, message):
        try:
            self.client.publish(topic, msg=message)
            print('published')
        except:
            self.reconnect()
            pass
```