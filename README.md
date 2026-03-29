# 天气数据采集与存储项目

## 项目简介
本项目基于 Python 开发，通过调用 OpenWeatherMap API 获取城市实时天气数据，并将温度、体感温度、湿度、气压等指标存储到 SQLite 数据库中，同时支持日志记录和基础可视化展示。

## 技术栈
- Python
- Requests
- SQLite
- Matplotlib

## 功能说明
1. 调用 OpenWeatherMap API 获取实时天气数据
2. 提取温度、体感温度、湿度、气压等字段
3. 将天气数据存储到 SQLite 数据库
4. 输出日志文件，记录运行情况
5. 生成天气数据柱状图
6. 支持查询历史天气记录

## 项目结构
```text
天气项目/
├─ weather_data.py
├─ check_db.py
├─ weather_data.db
├─ data_collection.log
├─ requirements.txt
└─ README.md