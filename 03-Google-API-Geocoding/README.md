# Geocoding and Map Visualization Explorer

A Python application that transforms addresses into geographic coordinates and displays them on an interactive map using Google's Geocoding API. This project demonstrates API integration, data persistence, and web visualization techniques.

## Project Overview

I built this application to explore:
- How to work with external APIs and handle their responses
- Techniques for storing and retrieving geographic data
- Methods for visualizing location data on interactive maps
- Best practices for error handling and rate limiting

The system follows a three-step process:
1. **Data Collection**: Retrieve geographic information from Google's Geocoding API
2. **Data Storage**: Save the retrieved data in a structured SQLite database
3. **Visualization**: Present the data visually on an interactive Google Map

## Key Features

- **Address to Coordinate Conversion**: Transforms text addresses into latitude/longitude coordinates
- **Data Persistence**: Stores retrieved data in SQLite to minimize API calls
- **Interactive Map Display**: Visualizes all locations on a Google Map with information windows
- **Error Handling**: Comprehensive error handling for API failures
- **Rate Limiting**: Built-in pauses to respect API rate limits

## Technical Implementation

### Technologies Used
- **Python**: Core application logic and data processing
- **SQLite**: Local database for storing geocoding results
- **Google Maps API**: Geographic data retrieval and map visualization
- **HTML/JavaScript**: Frontend map display

### Code Structure
- `geoload.py`: Fetches geographic data from the API and stores it in the database
- `geodump.py`: Extracts data from the database and formats it for visualization
- `where.html`: Web page that displays the locations on an interactive map
- `geodata.sqlite`: SQLite database that stores the geocoding results

## How to Use

### Prerequisites
- Python 3.x
- Internet connection
- (Optional) Google Maps API key for production use

### Setup
1. If you want to use the official Google API (recommended for production), get an API key from the [Google Cloud Platform Console](https://console.cloud.google.com/).
2. Open `geoload.py` and replace the placeholder API key with your own key.
3. Create a file named `where.data` with addresses, one per line.

### Running the Application
Follow these steps in order:

1. **Load the geographic data**:
   ```
   python geoload.py
   ```
   This will read addresses from `where.data` and store their geographic information in the database.

2. **Extract and format the data**:
   ```
   python geodump.py
   ```
   This will create a JavaScript file (`where.js`) containing the location data.

3. **View the map**:
   Open `where.html` in a web browser to see the locations displayed on a Google Map.

## What I Learned

This project helped me understand:
- How to integrate with external APIs and handle JSON responses
- Database operations for data persistence
- Error handling strategies for web requests
- Rate limiting techniques to respect API constraints
- Combining backend data processing with frontend visualization
- Working with geographic data and map systems

## Future Enhancements

I plan to expand this project by:
- Adding cluster markers for locations in close proximity
- Implementing search functionality for the map
- Creating a more interactive UI with filtering options
- Supporting additional geographic data sources
- Adding more visualizations like heat maps and route planning

## Notes and Limitations

- The application limits data retrieval to 200 locations at a time to prevent excessive API usage
- There's a built-in pause every 10 requests to respect API rate limits
- The project can use a fallback educational API if no Google API key is provided
- For production use, always use your own Google API key and follow Google's terms of service

