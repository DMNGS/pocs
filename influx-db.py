from influxdb import InfluxDBClient

client = InfluxDBClient(host='sdmansion.local', port=8086, username='patchouli', password='koakoakuma', ssl=True, verify_ssl=True)

print(client.get_list_database())