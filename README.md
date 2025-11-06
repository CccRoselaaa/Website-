# Flask Website Project

A simple website built using Flask (Python) with a MySQL database.

1. Requirements
Before running the project, install these Python packages:

pip install flask
pip install flask-sqlalchemy
pip install mysql-connector-python

2. Setting Up the Database

This project uses MySQL.
For security reasons, the database password is not included in the uploaded code. Before continuing with the next steps, the user must run the command below to start a MySQL server and create the database:

Run the command inside your terminal:
    
    docker run --name mysql-db -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=testdb -p 3306:3306 -d mysql:latest


3. Creating Tables

After Docker starts successfully, run the file: " Database Creation.py " This file generates all required tables used in the website. If there are no errors, your database is ready to use.

4. Running the Website

Once the database is set up, run inside the terminal: 
    python main.py
Inside the terminal should be a link that you can follow (' http://127.0.0.1:5000/ ')
The website should be running.

Bonus: Database Export Included
A MySQL export named testdb.sql is included in the repository.
You can import it manually into MySQL Workbench or another database tool if needed.