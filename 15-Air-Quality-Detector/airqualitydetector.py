from tkinter import *
from tkinter import ttk
import requests
import json
from PIL import ImageTk, Image
from datetime import datetime
import pytz

class AirQualityApp:
	def __init__(self, root):
		self.root = root
		self.root.title("Air Quality Detector - India")
		self.root.geometry("800x600")
		self.root.configure(bg="#f0f0f0")
		
		# OpenWeatherMap API Key
		self.api_key = "YOUR_API_KEY_HERE"  # Replace with your API key
		
		# List of Indian cities with their coordinates
		self.indian_cities = {
			"Delhi": {"lat": 28.6139, "lon": 77.2090},
			"Mumbai": {"lat": 19.0760, "lon": 72.8777},
			"Bangalore": {"lat": 12.9716, "lon": 77.5946},
			"Chennai": {"lat": 13.0827, "lon": 80.2707},
			"Kolkata": {"lat": 22.5726, "lon": 88.3639},
			"Hyderabad": {"lat": 17.3850, "lon": 78.4867},
			"Pune": {"lat": 18.5204, "lon": 73.8567},
			"Ahmedabad": {"lat": 23.0225, "lon": 72.5714},
			"Jaipur": {"lat": 26.9124, "lon": 75.7873},
			"Lucknow": {"lat": 26.8467, "lon": 80.9462}
		}
		
		# Create UI elements
		self.create_widgets()
		
		# Set default city and get data
		self.city_combobox.current(0)
		self.get_air_quality()

	def create_widgets(self):
		# Title
		title_label = Label(self.root, text="India Air Quality Monitor", font=("Helvetica", 24, "bold"), bg="#f0f0f0", fg="#333333")
		title_label.pack(pady=10)
		
		# Frame for city selection
		city_frame = Frame(self.root, bg="#f0f0f0")
		city_frame.pack(pady=10)
		
		city_label = Label(city_frame, text="Select City:", font=("Helvetica", 12), bg="#f0f0f0")
		city_label.pack(side=LEFT, padx=5)
		
		self.city_combobox = ttk.Combobox(city_frame, values=list(self.indian_cities.keys()), width=20, font=("Helvetica", 12))
		self.city_combobox.pack(side=LEFT, padx=5)
		
		refresh_button = Button(city_frame, text="Refresh Data", command=self.get_air_quality, bg="#4CAF50", fg="white", font=("Helvetica", 10), padx=10)
		refresh_button.pack(side=LEFT, padx=10)
		
		# Frame for AQI display
		self.aqi_frame = Frame(self.root, bg="#f0f0f0")
		self.aqi_frame.pack(pady=10)
		
		# Frame for pollutant details
		self.details_frame = Frame(self.root, bg="#f0f0f0", relief=RIDGE, bd=1)
		self.details_frame.pack(pady=10, padx=20, fill=X)
		
		# Frame for weather data
		self.weather_frame = Frame(self.root, bg="#f0f0f0")
		self.weather_frame.pack(pady=10, fill=X, padx=20)
		
		# Status bar for last updated
		self.status_bar = Label(self.root, text="", bd=1, relief=SUNKEN, anchor=W, font=("Helvetica", 8))
		self.status_bar.pack(side=BOTTOM, fill=X)

	def get_air_quality(self):
		selected_city = self.city_combobox.get()
		lat = self.indian_cities[selected_city]["lat"]
		lon = self.indian_cities[selected_city]["lon"]
		
		# Clear previous data
		for widget in self.aqi_frame.winfo_children():
			widget.destroy()
		
		for widget in self.details_frame.winfo_children():
			widget.destroy()
			
		for widget in self.weather_frame.winfo_children():
			widget.destroy()
		
		try:
			# Get air quality data
			air_quality_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={self.api_key}"
			air_response = requests.get(air_quality_url)
			air_data = json.loads(air_response.content)
			
			# Get weather data
			weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.api_key}&units=metric"
			weather_response = requests.get(weather_url)
			weather_data = json.loads(weather_response.content)
			
			# Parse data
			aqi = air_data["list"][0]["main"]["aqi"]
			components = air_data["list"][0]["components"]
			
			# Set AQI label and color
			aqi_category, aqi_color, health_msg = self.get_aqi_info(aqi)
			
			aqi_value_label = Label(self.aqi_frame, text=f"AQI: {aqi}", font=("Helvetica", 36, "bold"), bg=aqi_color, fg="white", padx=20, pady=10)
			aqi_value_label.pack()
			
			aqi_category_label = Label(self.aqi_frame, text=aqi_category, font=("Helvetica", 18), bg=aqi_color, fg="white", padx=20, pady=5)
			aqi_category_label.pack()
			
			health_label = Label(self.aqi_frame, text=health_msg, font=("Helvetica", 10), bg="#f0f0f0", wraplength=600, justify=CENTER, pady=5)
			health_label.pack()
			
			# Display pollutant details
			detail_title = Label(self.details_frame, text="Air Pollutants (μg/m³)", font=("Helvetica", 14, "bold"), bg="#f0f0f0")
			detail_title.grid(row=0, column=0, columnspan=4, pady=5, sticky=W)
			
			# PM2.5
			Label(self.details_frame, text="PM2.5:", font=("Helvetica", 12, "bold"), bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5, sticky=W)
			pm25_label = Label(self.details_frame, text=f"{components['pm2_5']:.1f}", font=("Helvetica", 12), bg="#f0f0f0")
			pm25_label.grid(row=1, column=1, padx=10, pady=5, sticky=W)
			
			# PM10
			Label(self.details_frame, text="PM10:", font=("Helvetica", 12, "bold"), bg="#f0f0f0").grid(row=1, column=2, padx=10, pady=5, sticky=W)
			pm10_label = Label(self.details_frame, text=f"{components['pm10']:.1f}", font=("Helvetica", 12), bg="#f0f0f0")
			pm10_label.grid(row=1, column=3, padx=10, pady=5, sticky=W)
			
			# NO2
			Label(self.details_frame, text="NO₂:", font=("Helvetica", 12, "bold"), bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=5, sticky=W)
			no2_label = Label(self.details_frame, text=f"{components['no2']:.1f}", font=("Helvetica", 12), bg="#f0f0f0")
			no2_label.grid(row=2, column=1, padx=10, pady=5, sticky=W)
			
			# SO2
			Label(self.details_frame, text="SO₂:", font=("Helvetica", 12, "bold"), bg="#f0f0f0").grid(row=2, column=2, padx=10, pady=5, sticky=W)
			so2_label = Label(self.details_frame, text=f"{components['so2']:.1f}", font=("Helvetica", 12), bg="#f0f0f0")
			so2_label.grid(row=2, column=3, padx=10, pady=5, sticky=W)
			
			# O3
			Label(self.details_frame, text="O₃:", font=("Helvetica", 12, "bold"), bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=5, sticky=W)
			o3_label = Label(self.details_frame, text=f"{components['o3']:.1f}", font=("Helvetica", 12), bg="#f0f0f0")
			o3_label.grid(row=3, column=1, padx=10, pady=5, sticky=W)
			
			# CO
			Label(self.details_frame, text="CO:", font=("Helvetica", 12, "bold"), bg="#f0f0f0").grid(row=3, column=2, padx=10, pady=5, sticky=W)
			co_label = Label(self.details_frame, text=f"{components['co']:.1f}", font=("Helvetica", 12), bg="#f0f0f0")
			co_label.grid(row=3, column=3, padx=10, pady=5, sticky=W)
			
			# Display weather data
			weather_title = Label(self.weather_frame, text="Current Weather", font=("Helvetica", 14, "bold"), bg="#f0f0f0")
			weather_title.grid(row=0, column=0, columnspan=4, pady=5, sticky=W)
			
			# Temperature
			Label(self.weather_frame, text="Temperature:", font=("Helvetica", 12, "bold"), bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5, sticky=W)
			temp_label = Label(self.weather_frame, text=f"{weather_data['main']['temp']:.1f}°C", font=("Helvetica", 12), bg="#f0f0f0")
			temp_label.grid(row=1, column=1, padx=10, pady=5, sticky=W)
			
			# Humidity
			Label(self.weather_frame, text="Humidity:", font=("Helvetica", 12, "bold"), bg="#f0f0f0").grid(row=1, column=2, padx=10, pady=5, sticky=W)
			humidity_label = Label(self.weather_frame, text=f"{weather_data['main']['humidity']}%", font=("Helvetica", 12), bg="#f0f0f0")
			humidity_label.grid(row=1, column=3, padx=10, pady=5, sticky=W)
			
			# Wind
			Label(self.weather_frame, text="Wind Speed:", font=("Helvetica", 12, "bold"), bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=5, sticky=W)
			wind_label = Label(self.weather_frame, text=f"{weather_data['wind']['speed']} m/s", font=("Helvetica", 12), bg="#f0f0f0")
			wind_label.grid(row=2, column=1, padx=10, pady=5, sticky=W)
			
			# Weather condition
			Label(self.weather_frame, text="Condition:", font=("Helvetica", 12, "bold"), bg="#f0f0f0").grid(row=2, column=2, padx=10, pady=5, sticky=W)
			condition_label = Label(self.weather_frame, text=f"{weather_data['weather'][0]['description'].title()}", font=("Helvetica", 12), bg="#f0f0f0")
			condition_label.grid(row=2, column=3, padx=10, pady=5, sticky=W)
			
			# Update status bar
			india_timezone = pytz.timezone('Asia/Kolkata')
			now = datetime.now(india_timezone)
			self.status_bar.config(text=f"Last Updated: {now.strftime('%d-%m-%Y %H:%M:%S')} IST | Data Source: OpenWeatherMap")
			
		except Exception as e:
			error_label = Label(self.aqi_frame, text=f"Error: {str(e)}", font=("Helvetica", 14), bg="#f0f0f0", fg="red")
			error_label.pack(pady=20)
			self.status_bar.config(text=f"Error occurred while fetching data. Please check your API key and internet connection.")

	def get_aqi_info(self, aqi):
		if aqi == 1:
			return "Good", "#4CAF50", "Air quality is considered satisfactory, and air pollution poses little or no risk."
		elif aqi == 2:
			return "Fair", "#8BC34A", "Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
		elif aqi == 3:
			return "Moderate", "#FFC107", "Members of sensitive groups may experience health effects. The general public is less likely to be affected."
		elif aqi == 4:
			return "Poor", "#FF9800", "Everyone may begin to experience health effects. Members of sensitive groups may experience more serious health effects."
		elif aqi == 5:
			return "Very Poor", "#F44336", "Health alert: The risk of health effects is increased for everyone. Everyone may experience more serious health effects."
		else:
			return "Unknown", "#9E9E9E", "No data available."

if __name__ == "__main__":
	root = Tk()
	app = AirQualityApp(root)
	root.mainloop()

