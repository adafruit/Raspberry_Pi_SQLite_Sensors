# Raspberry Pi SQLite Database Sensor Readings pt. 1
# This code will read a SQLite database and use it to configure a number of
# DHT temperature/humidity to log readings to the database.  You must create the
# database ahead of time with the following commands/table schema:
# - Store configured sensors in a 'sensors' table:
#   CREATE TABLE sensors (name TEXT, type TEXT, pin INTEGER);
# - Store sensor readings in a 'readings' table:
#   CREATE TABLE readings (time DATETIME, name TEXT, value REAL);
# Author: Tony DiCola
# License: Public Domain
import sqlite3
import time

import Adafruit_DHT


# Open SQLite database and create a cursor for later queries.
conn = sqlite3.connect('dht.db')
c = conn.cursor()

# Read all the configured sensors from the DB.
c.execute('SELECT name, type, pin FROM sensors')
sensors = []
for row in c:
    name, dht_type, pin = row
    print('Configuring sensor: {0} of type: {1} on pin: {2}'.format(name, dht_type, pin))
    # Convert DHT type from string to DHT library value.
    if dht_type == 'DHT22':
        dht_type = Adafruit_DHT.DHT22
    elif dht_type == 'DHT11':
        dht_type = Adafruit_DHT.DHT11
    else:
        raise RuntimeError('Unknown sensor type: {0}'.format(dht_type))
    # Save the sensor into the list of configured sensors.
    sensors.append((name, dht_type, pin))

# Main loop to read each sensor and save the readings in the database.
print('Saving sensor data every two seconds (press Ctrl-C to quit)...')
while True:
    # Save the current unix time for this measurement.
    reading_time = int(time.time())
    # Go through each sensor and take a reading.
    for s in sensors:
        name, dht_type, pin = s
        humidity, temperature = Adafruit_DHT.read_retry(dht_type, pin)
        print('Read sensor: {0} humidity: {1:0.2f}% temperature: {2:0.2f}C'.format(name, humidity, temperature))
        # Save the reading in the readings table.
        c.execute('INSERT INTO readings VALUES (?, ?, ?)',
                  (reading_time, '{0} Humidity'.format(name), humidity))
        c.execute('INSERT INTO readings VALUES (?, ?, ?)',
                  (reading_time, '{0} Temperature'.format(name), temperature))
        conn.commit()
    time.sleep(2.0)
