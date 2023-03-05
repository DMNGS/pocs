# Script      : dbcon.py
# Description : databse connector
# Author      : DOMINGUES PEDROSA Samuel
# Date        : 2023.02.16, V1.0
from influxdb import InfluxDBClient
from dotenv import load_dotenv
import os

load_dotenv()

class DbCon:
    """
    A MariaDB databse connector

    Attributes
    ----------
    client : InfluxDBClient
        the connector to the databse

    Methods
    -------
    select(table)
        Get all values from table
    """

    def __init__(self):
        load_dotenv()
        host = os.getenv('DB_HOST')
        port = os.getenv('DB_PORT')
        user = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
        database = os.getenv('DB_DATABASE')
        self.client = InfluxDBClient(host, port, user, password, database)
    pass

    def select_all(self):
        """
        Get all values from the measurement

        Returns
        -------
        ResultSet
            the result of the query
        """
        data = self.client.query(f'SELECT time,topic,value FROM mqtt_consumer')
        return data

    def select_topic(self, topic):
        """
        Get values from table

        Parameters
        ----------
        topic: str
            the topic
        Returns
        -------
        ResultSet
            the result of the query
        """
        data = self.client.query(f'SELECT time,topic,value FROM mqtt_consumer WHERE topic={topic}')
        return data

    def get_topics(self):
        values = dict()
        serie = self.select_all()
        for val in serie.raw['series'][0]['values']:
            if not val[1] in values:
                values[val[1]] = []
            values[val[1]].append({'time': val[0], 'value': val[2]})

        return values