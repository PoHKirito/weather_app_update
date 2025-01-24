from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
db_path = "weather_forecast.db"  # SQLite 数据库路径

@app.route('/forecast', methods=['POST'])
def get_forecast():
    data = request.json
    area_code = data.get('area_code')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    response_data = []

    if not area_code or not start_date or not end_date:
        return jsonify({"error": "すべてのフィールドを入力してください。"})

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        query = '''
            SELECT date, area_name, weather, temperature, precipitation, wind, wave 
            FROM weather_reports 
            WHERE area_code = ? AND date BETWEEN ? AND ?
        '''
        cursor.execute(query, (area_code, start_date, end_date))
        rows = cursor.fetchall()

        for row in rows:
            response_data.append({
                "Date": row[0],
                "Area": row[1],
                "Weather": row[2],
                "Temperature": row[3],
                "Precipitation": row[4],
                "Wind": row[5],
                "Wave": row[6],
            })
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        conn.close()

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
