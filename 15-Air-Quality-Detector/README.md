# India Air Quality Detector

A desktop application that provides real-time air quality information for major Indian cities.

## Features

- Real-time Air Quality Index (AQI) monitoring for 10 major Indian cities
- Detailed pollution parameters (PM2.5, PM10, NO2, SO2, O3, CO)
- Current weather information (temperature, humidity, wind, conditions)
- Color-coded AQI display with health recommendations
- Easy city selection with dropdown menu
- Automatic timestamp in Indian Standard Time (IST)

## Screenshots

(Add screenshots of your application here)

## Requirements

- Python 3.6 or higher
- Required Python packages:
  - tkinter
  - requests
  - PIL (Pillow)
  - pytz

## Installation

1. Clone or download this repository
2. Install the required packages:
   ```
   pip install requests pillow pytz
   ```
3. Open `airqualitydetector.py` and replace "YOUR_API_KEY_HERE" with your OpenWeatherMap API key
4. Run the application:
   ```
   python airqualitydetector.py
   ```

## How to Get an API Key

1. Create a free account at [OpenWeatherMap](https://openweathermap.org/)
2. Go to your account page and navigate to the "API keys" tab
3. Generate a new API key or use your existing one
4. The free tier allows up to 1,000 API calls per day

## Data Sources

This application uses data from:
- [OpenWeatherMap Air Pollution API](https://openweathermap.org/api/air-pollution)
- [OpenWeatherMap Current Weather API](https://openweathermap.org/current)

## Credits

This application was developed as a Python project for monitoring air quality specifically in Indian cities. 