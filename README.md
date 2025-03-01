# API-INTEGRATION-AND-DATA-VISUALIZATION

"COMPANY": CODTECH IT SOLUTIONS

"NAME": KRISHKANTH K

"INTERN ID": CT08TUV

"DOMAIN": PYTHON 

"DURATION": 4 WEEKS

"MENTOR": NEELA SANTOSH



Weather Forecast Visualization

Introduction

This project fetches and visualizes weather forecast data using the OpenWeatherMap API. It allows users to analyze temperature and humidity trends for a specified city over a forecast period. The data is processed and visualized using Pandas and Matplotlib.

Features

Fetches weather forecast data from OpenWeatherMap.

Processes and structures data into a Pandas DataFrame.

Converts date strings into a proper datetime format for plotting.

Generates a line plot showing temperature trends over time.

Creates a bar chart representing humidity levels.

Displays raw weather data in a tabular format for reference.


Prerequisites

Before running this script, ensure you have the following installed:

Python 3.x


Required Python libraries:

pip install requests pandas matplotlib


Setup Instructions

Clone the Repository

git clone https://github.com/your-username/weather-forecast-visualization.git
cd weather-forecast-visualization


Obtain an API Key

Sign up at OpenWeatherMap and generate an API key.

Replace the API_KEY placeholder in the script with your actual key.

Modify City Name (Optional)

By default, the script fetches weather data for India. Modify the CITY variable to specify a different location.


Run the Script

python weather_visualization.py


Code Breakdown

Fetching Weather Data

The script sends a request to the OpenWeatherMap API and retrieves weather forecast data in JSON format.

response = requests.get(URL)
data = response.json()


Processing Data

The JSON response is converted into a structured Pandas DataFrame, extracting relevant fields such as date, temperature, and humidity.

df = pd.DataFrame([{
    "Date": item["dt_txt"],
    "Temperature": item["main"]["temp"],
    "Humidity": item["main"]["humidity"]
} for item in data["list"]])


Data Visualization

The script generates two visualizations:

Temperature Trend: A line graph showing temperature variations over time.

Humidity Levels: A bar chart displaying humidity levels for the forecasted period.

plt.plot(df["Date"], df["Temperature"], marker="o", linestyle="-")
plt.bar(df["Date"], df["Humidity"], color="skyblue")


Displaying Raw Data

The processed DataFrame is printed in tabular format for reference.

print(df)


Example Output

After running the script, you will see:

Temperature Trend Plot: A visual representation of how temperature fluctuates over time.

Humidity Levels Chart: A bar chart depicting humidity variations.

Raw Weather Data: A table displaying structured weather data.


Troubleshooting

If you receive an error regarding API authentication, ensure that you have correctly set your API key.

If the script fails to fetch data, verify that the specified city name is valid.

Ensure you have an active internet connection.


Future Enhancements

Add interactive visualizations using Plotly.

Implement a GUI for selecting cities dynamically.

Support multiple cities for comparison.

Store historical weather data for trend analysis.
