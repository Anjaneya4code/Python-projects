Weather Information App 🌦️
A simple Python-based weather application that fetches live weather information using the OpenWeather API.
Features
- Search weather by city name
- Displays temperature and feels-like temperature
- Shows humidity
- Shows weather condition
- Shows wind speed
- Displays country code
- Handles invalid city/API requests
Technologies
- Python
- Requests library
- OpenWeather API
Installation
pip install requests
Setup
1. Create an account on OpenWeather and generate an API key.
2. Open the Python file.
3. Replace:
API_KEY = "YOUR_API_KEY"
with your actual API key.
Run
python weather.py
Enter a city name when prompted.
Example
Enter city name: Delhi

===== WEATHER INFORMATION =====
City: Delhi
Country: IN
Temperature: 31.5 °C
Feels Like: 34.2 °C
Humidity: 58 %
Weather: clear sky
Wind Speed: 2.6 m/s
Project Purpose
This project demonstrates how Python can communicate with a real-world REST API, process JSON data, and display useful information to the user.
