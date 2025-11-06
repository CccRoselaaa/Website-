import mysql.connector

# Connect to SQL server
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port=3306
)

mycursor = db.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS testdb;")

mycursor.close()
db.close()

# Connect to created database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root", 
    database="testdb",
    port=3306
)

mycursor = db.cursor()

mycursor.execute("""
    CREATE TABLE IF NOT EXISTS Sport (
        sport_id INT AUTO_INCREMENT PRIMARY KEY,
        sport_name VARCHAR(40)
    );
""")


mycursor.execute("""
    CREATE TABLE IF NOT EXISTS Event (
        event_id INT AUTO_INCREMENT PRIMARY KEY,
        event_location VARCHAR(30) NOT NULL,
        event_date DATE NOT NULL,
        event_time TIME NOT NULL
    );
""")


mycursor.execute("""
    CREATE TABLE IF NOT EXISTS Team (
        team_id INT AUTO_INCREMENT PRIMARY KEY,
        team_name VARCHAR(40) NOT NULL,
        _sport_id INT NOT NULL,
        FOREIGN KEY (_sport_id) REFERENCES Sport(sport_id)
    );
""")


mycursor.execute("""
    CREATE TABLE IF NOT EXISTS Game (
        game_id INT AUTO_INCREMENT PRIMARY KEY,
        _team1 INT NOT NULL,
        _team2 INT NOT NULL,
        _sport_id INT NOT NULL,
        _event_id INT NOT NULL,
        FOREIGN KEY (_team1) REFERENCES Team(team_id),
        FOREIGN KEY (_team2) REFERENCES Team(team_id),
        FOREIGN KEY (_sport_id) REFERENCES Sport(sport_id),
        FOREIGN KEY (_event_id) REFERENCES Event(event_id)
    );
""")
