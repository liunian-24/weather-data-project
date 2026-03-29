import requests
import sqlite3
import logging
import matplotlib.pyplot as plt

# 设置日志配置
logging.basicConfig(
    filename='data_collection.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# 你的 API 密钥和城市
API_KEY = 'c7f7f6d4547ef51b50bbc2a8f2ab3129'
CITY = 'Shanghai'

# 请求 URL
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}'


# 显示图表的函数
def show_chart(labels, values):
    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, values, edgecolor='black')

    plt.title(f'Weather Data for {CITY}')
    plt.ylabel('Value')
    plt.ylim(0, max(values) + 10)

    # 在每个柱子上显示数值
    for i, v in enumerate(values):
        plt.text(i, v + 1, str(round(v, 2)), ha='center', va='bottom', fontsize=10)

    plt.tight_layout()
    plt.show()


# 定义获取并存储天气数据的函数
def fetch_and_store_weather():
    try:
        response = requests.get(URL, timeout=10)

        if response.status_code == 200:
            data = response.json()
            logging.info(f"Successfully fetched weather data for {CITY}")

            # 提取返回的数据
            temperature = data['main']['temp'] - 273.15
            feels_like = data['main']['feels_like'] - 273.15
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']

            print("成功获取天气数据：")
            print(data)

            # 连接到 SQLite 数据库
            conn = sqlite3.connect('weather_data.db')
            cursor = conn.cursor()

            # 创建表格
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS weather (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT,
                temperature REAL,
                feels_like REAL,
                humidity INTEGER,
                pressure INTEGER
            )
            ''')

            # 插入天气数据
            cursor.execute('''
            INSERT INTO weather (city, temperature, feels_like, humidity, pressure)
            VALUES (?, ?, ?, ?, ?)
            ''', (CITY, temperature, feels_like, humidity, pressure))

            conn.commit()
            conn.close()

            logging.info(f"Data for {CITY} successfully stored in the database.")
            print("数据已成功存入数据库 weather_data.db")

            # 可视化天气数据
            labels = ['Temperature (°C)', 'Feels Like (°C)', 'Humidity (%)', 'Pressure (hPa)']
            values = [temperature, feels_like, humidity, pressure]
            show_chart(labels, values)

        else:
            logging.error(f"Failed to fetch data for {CITY}, status code: {response.status_code}")
            print(f"请求失败，状态码：{response.status_code}")
            print(response.text)

    except Exception as e:
        logging.error(f"Program error: {e}")
        print("程序运行出错：", e)


if __name__ == "__main__":
    fetch_and_store_weather()