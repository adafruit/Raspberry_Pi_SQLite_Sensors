# Raspberry Pi SQLite Database Sensor Readings pt. 4
# Basic flask application that uses flask-admin to generate handy web interfaces
# to manipulate the sensor config and readings from the database.
# Author: Tony DiCola
# License: Public Domain
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView

import model


# Create a basic flask app.
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mosfet'  # You should probably change this to a random value!
# Add the DHT data model to the app config so templates can reach it and query
# the sensors & readings.
app.config['MODEL'] = model.DHTData()

# Add an admin view for the Peewee ORM-based DHT sensor and sensor reading models.
admin = Admin(app, name='SQLite Sensors', template_mode='bootstrap3', url='/')
admin.add_view(ModelView(model.DHTSensor))
admin.add_view(ModelView(model.SensorReading))
