# Raspberry Pi SQLite Sensors pt. 2

This example builds on pt. 1 to show how to use SQLite with the Peewee ORM
(object relational mapper).  Using an ORM can simplify your code to talk to
databases and even remove much of the need to manually write and run SQL queries.

## Setup

Make sure you've followed part 1 and have setup the hardware and Python 3 as
described.  Then issue the following command to install the Peewee ORM (from
http://docs.peewee-orm.com/en/latest/):

    sudo pip3 install peewee

## Usage

Modify dht_read.py to define the DHT sensors you have connected to your hardware
(i.e. change the data.define_sensor function calls as appropriate).  Then run
the dht_read.py as root and it will automatically create the dht.db database,
populate it with the defined sensors, and then loop taking sensor readings every
two seconds.  For example run with:

    sudo python3 dht_read.py

That's it!
