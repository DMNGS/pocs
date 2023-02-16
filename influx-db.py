# Script      : dbcon.py
# Description : databse connector
# Author      : DOMINGUES PEDROSA Samuel
# Date        : 2023.02.16, V1.0
from influxdb import InfluxDBClient

class DbChef:
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

    def select(table):
        """
        Get all values from table

        Parameters
        ----------
        table: str
            the table
        Returns
        -------
        ResultSet
            the result of the query
        """
        data = self.client.query(f'SELECT * FROM {table}')
        return data

client = InfluxDBClient('testbench.local', 8086, 'graphana', 'lmp2020', 'home')