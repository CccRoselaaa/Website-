# Flask Website Project

A simple website built using Flask (Python) with a MySQL database.

Assumptions:

The database structure was designed with the following logic in mind:

        In the Sport table, one sport can have many teams and many games.
        
        In the Team table, each team belongs to one specific sport but can participate in multiple games.
        
        In the Event table, each event hosts exactly one game, including its location, date, and time.
        
        In the Game table, each game connects two teams, one sport, and one event.

I used SQLAlchemy reflection instead of defining manually ORM models, as it already allowed me to map the existing tables I had already created in MySQL.

To make the project easier to test, I used Docker to create a local MySQL server (instructions on: 2. Setting Up the Database).

1. Requirements

Before running the project, install these Python packages:

        pip install flask
    
        pip install flask-sqlalchemy
    
        pip install mysql-connector-python

2. Setting Up the Database

This project uses MySQL.
For security reasons, the database password is not included in the uploaded code. Before continuing with the next steps, the user must run the command below to start a MySQL server and create the database:

Run the command inside the terminal:
    
    docker run --name mysql-db -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=testdb -p 3306:3306 -d mysql:latest


3. Creating Tables

After Docker starts successfully, run the file: " Database Creation.py ". This file generates all the required tables used for the website. If there are no errors, the database is ready to use.

4. Running the Website

Once the database is set up, run inside the terminal: 
    python main.py
Inside the terminal should be a link: (' http://127.0.0.1:5000/ ')
The website should be running.

Bonus: Database Export Included

A MySQL export named testdb.sql is included in the repository.
Can be imported manually into MySQL Workbench or another database tool if needed.
