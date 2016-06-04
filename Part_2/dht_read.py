# Raspberry Pi SQLite Database Sensor Readings pt. 2
# This code will use the Peewee ORM to simplfiy access to a SQLite database.
# The functionality is exactly the same as in pt. 1, but notice how much simpler
# the code is by using a data model abstraction and the ORM.
# Author: Tony DiCola
# License: Public Domain
import datetime
import time

import Adafruit_DHT

import model


# Create an instance of our data model access layer object.
# This object takes care of all the Peewee ORM and DB access so our code in this
# file is very simple and just calls function on the model access layer object.
data = model.DHTData()

# Define which sensors we expect to be connected to the Pi.
data.define_sensor('DHT1', Adafruit_DHT.DHT22, 18)
data.define_sensor('DHT2', Adafruit_DHT.DHT22, 25)

# Main loop to take sensor readings every two seconds.
try:
    while True:
        # Get the current time for this batch of sensor readings.
        reading_time = datetime.datetime.now()
        # Go through each sensor and get its current reading.
        for sensor in data.get_sensors():
            # Get a DHT sensor reading and print it out.
            humidity, temperature = Adafruit_DHT.read_retry(sensor.dht_type, sensor.pin)
            print('Read sensor: {0} humidity: {1:0.2f}% temperature: {2:0.2f}C'.format(sensor.name, humidity, temperature))
            # Add the sensor reading to the database.
            data.add_reading(time=reading_time, name='{0} Humidity'.format(sensor.name), value=humidity)
            data.add_reading(time=reading_time, name='{0} Temperature'.format(sensor.name), value=temperature)
        # Wait 2 seconds and repeat.
        time.sleep(2.0)
finally:
    # Finally close the connection to the database when done.
    data.close()
