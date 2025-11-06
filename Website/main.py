from flask import Flask, render_template, request, redirect
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Connect to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Prezenca44$@localhost/testdb'
db = SQLAlchemy(app)

# Reflect existing tables from db
with app.app_context():
    db.metadata.reflect(db.engine)

Event = db.metadata.tables['event']
Game = db.metadata.tables['game']
Team = db.metadata.tables['team']
Sport = db.metadata.tables['sport']

# Home Page 
@app.route("/")
def home():
    with db.engine.connect() as connection:
        query = """
        SELECT g.game_id, e.event_date, e.event_time, e.event_location
        FROM game g
        JOIN event e ON g._event_id = e.event_id
        ORDER BY e.event_date
        """
        games = connection.execute(db.text(query)).fetchall()
    return render_template('home.html', games=games)



@app.route("/add", methods=["POST", "GET"])
def game_add():
    if request.method == "POST":
        #Form data
        location = request.form["location"]
        date = request.form["date"]
        time = request.form["time"]
        sport_name = request.form["sport"]
        team1_name = request.form["team1"]
        team2_name = request.form["team2"]

        with db.engine.connect() as connection:
            # Incl. sport
            sport_result = connection.execute(
                text("SELECT sport_id FROM Sport WHERE sport_name = :s"),
                {"s": sport_name}
            ).fetchone()
            if sport_result:
                sport_id = sport_result[0]
            else:
                connection.execute(text("INSERT INTO Sport (sport_name) VALUES (:s)"), {"s": sport_name})
                sport_id = connection.execute(text("SELECT LAST_INSERT_ID()")).fetchone()[0]

            #Add event
            connection.execute(
                text("INSERT INTO Event (event_location, event_date, event_time) VALUES (:l, :d, :t)"),
                {"l": location, "d": date, "t": time}
            )
            event_id = connection.execute(text("SELECT LAST_INSERT_ID()")).fetchone()[0]

            #Add teams
            connection.execute(
                text("INSERT INTO Team (team_name, _sport_id) VALUES (:n, :s)"),
                {"n": team1_name, "s": sport_id}
            )
            team1_id = connection.execute(text("SELECT LAST_INSERT_ID()")).fetchone()[0]

            connection.execute(
                text("INSERT INTO Team (team_name, _sport_id) VALUES (:n, :s)"),
                {"n": team2_name, "s": sport_id}
            )
            team2_id = connection.execute(text("SELECT LAST_INSERT_ID()")).fetchone()[0]

            # Add game
            connection.execute(
                text("INSERT INTO Game (_team1, _team2, _sport_id, _event_id) VALUES (:t1, :t2, :s, :e)"),
                {"t1": team1_id, "t2": team2_id, "s": sport_id, "e": event_id}
            )

            connection.commit()

        return redirect("/")
    else:
        return render_template("add.html")

 
@app.route("/details/<int:game_id>")
def game_detail(game_id):
    from sqlalchemy import text
    with db.engine.connect() as conn:
        query = """
            SELECT e.event_date, e.event_time, e.event_location,
                   s.sport_name,
                   t1.team_name AS team1,
                   t2.team_name AS team2
            FROM Game g
            JOIN Event e ON g._event_id = e.event_id
            JOIN Sport s ON g._sport_id = s.sport_id
            JOIN Team t1 ON g._team1 = t1.team_id
            JOIN Team t2 ON g._team2 = t2.team_id
            WHERE g.game_id = :gid
        """
        result = conn.execute(text(query), {"gid": game_id}).fetchone()
    return render_template("details.html", game=result)

   
if __name__ == '__main__':
    app.run()