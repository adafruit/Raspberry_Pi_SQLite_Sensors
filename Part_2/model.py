# Raspberry Pi SQLite Database Sensor Readings pt. 2
# This code creates a basic data model for the project using the Peewee ORM to
# simplfiy access to a SQLite database.  The functionality is exactly the same
# as in pt. 1, but notice how the ORM removes the need to write SQL queries
# embedded in the code.
# Author: Tony DiCola
# License: Public Domain
from peewee import *


db = SqliteDatabase('dht.db')


# Define data model classes that inherit from the Peewee ORM Model class.
# Each of these classes will be represented by a table in the database that
# Peewee will create and manage.  Each row in the table is an instance of the
# model (like a DHT sensor config, sensor reading, etc).
class DHTSensor(Model):
    name = CharField()
    dht_type = IntegerField()
    pin = IntegerField()

    class Meta:
        database = db


class SensorReading(Model):
    time = DateTimeField()
    name = CharField()
    value = FloatField()

    class Meta:
        database = db


class DHTData(object):
    """Main data access layer class which provides functions to query DHT sensor
    and sensor reading data from the database.
    """

    def __init__(self):
        """Initialize access to the DHT sensor reading database."""
        # Connect to the database.
        db.connect()
        # Make sure the tables are created (safe=True, otherwise they might be
        # deleted!).
        db.create_tables([DHTSensor, SensorReading], safe=True)

    def define_sensor(self, name, dht_type, pin):
        """Define the specified sensor and add it to the database.  If a sensor
        of the same name, type, and pin exists then nothing will be added.
        """
        # Use the get_or_create function in Peewee to automatically try to find
        # a sensor the specified name, type, pin and create it if not found.
        # Very handy!
        DHTSensor.get_or_create(name=name, dht_type=dht_type, pin=pin)

    def get_sensors(self):
        """Return a list of all the DHT sensors defined in the database.
        Each instace in the list is a DHTSensor object.
        """
        # Use the select function to get all the sensors (effectively a SQL
        # SELECT * FROM... query).
        return DHTSensor.select()

    def add_reading(self, time, name, value):
        """Add the specified sensor reading to the database."""
        SensorReading.create(time=time, name=name, value=value)

    def close(self):
        """Close the connection to the database."""
        db.close()
