# Website
Website Creation using Flask, in Python

Requirements:
Need to install:
    pip install mysql
    pip install mysql-connector-python

    pip install flask
    pip install flask-sqlalchemy


Setting up the Database:
    For privacy reasons, i cannot share my exact database information here, as I would need to show in my code my password as well, so in order to create a database the user can use, before running the file called Database Creation, in the terminal type out: 
    
    docker run --name mysql-db -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=testdb -p 3306:3306 -d mysql:latest

    
This will create a MySQL server that can be used immediatly.


After creating the database (running the create database file, assuming there was no error), you should now be able to access the website created.

I'll be sharing as an export from MySQL, called testdb, which was the database that i created during development for this website.