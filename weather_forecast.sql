BEGIN TRANSACTION;
CREATE TABLE DetailedWeather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            area_code TEXT,
            date TEXT,
            time TEXT,
            weather TEXT,
            wind TEXT,
            wave TEXT,
            pop TEXT,
            temp_min TEXT,
            temp_max TEXT
        );
CREATE TABLE WeatherForecast (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            area_code TEXT,
            area_name TEXT,
            date TEXT,
            weather TEXT,
            temperature TEXT,
            precipitation TEXT,
            wind TEXT,
            wave TEXT
        );
DELETE FROM "sqlite_sequence";
COMMIT;
