import sqlite3

conn = sqlite3.connect('weather_data.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM weather")
rows = cursor.fetchall()

print("数据库中的天气记录：")
for row in rows:
    print(row)

conn.close()