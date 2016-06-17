# Raspberry Pi SQLite Sensors pt. 3

This example builds on pt. 1 and 2 to show how to build a simple flask web application
that displays sensor data and state stored in the SQLite database.  The flask-admin
extension is used to very quickly build a basic interface for manipulating the
database data.

## Setup

Make sure you've followed part 1 and 2 and have setup the hardware and Python 3 as
described.  Then issue the following command to install the flask web framework
and flask-admin plugin:

    sudo pip3 install flask flask-admin wtf-peewee

## Usage

Modify dht_read.py to define the DHT sensors you have connected to your hardware
(i.e. change the data.define_sensor function calls as appropriate).  Then run
the dht_read.py as root and it will automatically create the dht.db database,
populate it with the defined sensors, and then loop taking sensor readings every
two seconds.  For example run with:

    sudo python3 dht_read.py

Next to run the web application (you can open a new connection to the Pi so the
dht_read.py scripts keeps running in the background) run the following command:

    FLASK_APP=webapp.py flask run --host=0.0.0.0

NOTE: The above assumes you are using the very latest version of flask, if you
aren't then run the following to upgrade flask:

    sudo pip3 install flask --upgrade

You should see something like the following to indicate the web app is running
on port 5000:

    * Serving Flask app "webapp"
    * Forcing debug mode on
    * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)

Open a browser and navigate to http://raspberrypi:5000/ (note you might need to
use the IP address of your pi if your router doesn't resolve the hostname automatically).
