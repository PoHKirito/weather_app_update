from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

def initialize_database():
    conn = sqlite3.connect("weather_forecast.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS WeatherForecast (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            area_code TEXT,
            area_name TEXT,
            date TEXT,
            weather TEXT,
            temperature TEXT,
            precipitation TEXT,
            wind TEXT,
            wave TEXT
        )
    """)
    conn.commit()
    conn.close()

def export_to_sql():
    conn = sqlite3.connect("weather_forecast.db")
    with open("weather_forecast.sql", "w") as f:
        for line in conn.iterdump():
            f.write(f"{line}\n")
    conn.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/export", methods=["GET"])
def export_database():
    try:
        export_to_sql()
        return jsonify({"message": "Database exported to weather_forecast.sql"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)
