# Afficher les données d'une DB InfluxDB sur un site web Flask
Maintenant que le boker MQTT et la base de donnée InfluxDB sont en place, on a plus qu'a aller récupérer les données dans la DB et les afficher sur un site en Flask, une librairie Python qui permet de créer des sites web.

## Installer les librairies
On aura besoin de deux librairies, Flask et `influxdb` pour accéder à la DB.
```bash title="Installer flask et influxdb"
pip install flask influxdb
```

## Se connecter à InfluxDB et récupérer les topics

```python
from influxdb import InfluxDBClient

# Crée un client
client = InfluxDBClient(host, port, user, password, database)

# Selectionner toutes les valeurs
data = client.query(f'SELECT time,topic,value FROM mqtt_consumer')

# Afficher les enregistrement
for val in data.raw['series'][0]['values']:
    print(val)
```

