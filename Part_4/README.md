# Raspberry Pi SQLite Sensors pt. 4

This example builds on pt. 1, 2 and 3 to show how easy it is to move to a different
database engine like MySQL.  Because our application is built using an ORM layer
that abstracts access to the database it is very easy to change the underlying
database.  This is powerful as it allows you to more easily scale your application
by starting with a simple DB like SQLite and expanding later to a much more
feature rich database.

## Setup

Make sure you've followed part 1, 2, 3 and have setup the hardware and Python 3 as
described.  Then issue the following command to install the MySQL database server:

    sudo apt-get install -y mysql-server

During the installation it will prompt for a root user password.  Set a password
that you'll remember as it will be needed later in the code.

Finally install the PyMySQL library by running:

    sudo pip3 install PyMySQL

## Usage

First you will need to create a database named 'dht' on your MySQL server.
Connect to MySQL's command terminal by running:

    mysql -u root -p

Enter your password, then at the mysql> prompt run this command to create
a database called dht:

    create database dht;

If you'd ever like to remove the database (and completely lose all the data!)
you can run the drop database command:

    drop database dht;

Next modify model.py and update this line so it has the correct database name,
username, and password for your database:

    db = MySQLDatabase('dht', user='root', passwd='raspberry')

That's it!  The scripts like dht_read.py and webapp.py are run exactly as before
in parts 3 and 2.  However now both of them will use a MySQL database on the Pi
instead of the SQLite database.  This can allow for higher levels of performance
as the MySQL database is optimized for greater load compared to SQLite.  Notice
just how little code we had to change to support this too--only one line!
