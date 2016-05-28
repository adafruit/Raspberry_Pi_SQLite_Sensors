# Raspberry Pi SQLite Sensors pt. 1

This example will show how to create a basic SQLite database and use it to configured
sensors and store sensor readings.  This is built to use the DHT temperature/humidity
sensor and will need at least one connected to the Pi (see https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/wiring).

## Setup

First make sure you have Python 3 and a few dependencies installed on the Pi by
running (assuming Raspbian Jessie):

    sudo apt-get update
    sudo apt-get install -y python3 python3-dev python3-pip git sqlite3

Next install the DHT sensor Python library:

    git clone https://github.com/adafruit/Adafruit_Python_DHT.git
    cd Adafruit_Python_DHT
    sudo python3 setup.py install

## Database Setup

Inside the Part_1 folder use SQLite to create a database called dht.db:

    sqlite3 dht.db

At the SQL prompt issues the following create statements to create a table for
sensor readings, and a table for sensor configuration:

    CREATE TABLE readings (time DATETIME, name TEXT, value REAL);
    CREATE TABLE sensors (name TEXT, type TEXT, pin INTEGER);

Add a configured DHT sensor to the sensors table with an insert command (note
you can do this multiple times for multiple sensors):

    INSERT INTO sensors VALUES ('DHT1', 'DHT22', 18);

Change the values inside the parenthesis to the desird name (any string), the type
of DHT sensor (either 'DHT22' or 'DHT11' exactly), and the pin connected to the
sensor output.

## Usage

Once the database is created and sensors configured run the script as root like:

    sudo python3 dht_read.py

The script will read the configured DHT sensors every two seconds and store the
readings in the readings table.  You can use sqlite's command line console or
a graphical wrapper around it to query the database, for example to read all
the sensor readings execute:

    SELECT * FROM readings;

Or to just read sensor readings in the last minute (60 seconds):

    SELECT * FROM readings WHERE time >= strftime('%s', 'now')-60;
