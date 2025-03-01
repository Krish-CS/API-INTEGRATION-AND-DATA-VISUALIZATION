# API-INTEGRATION-AND-DATA-VISUALIZATION

**"COMPANY":** CODTECH IT SOLUTIONS

**"NAME":** KRISHKANTH K

**"INTERN ID":** CT08TUV

**"DOMAIN":** PYTHON PROGRAMMING

**"DURATION":** 4 WEEKS

**"MENTOR":** NEELA SANTHOSH KUMAR



**Weather Forecast Visualization**

**Introduction**

This project fetches and visualizes weather forecast data using the OpenWeatherMap API. It allows users to analyze temperature and humidity trends for a specified city over a forecast period. The data is processed and visualized using Pandas and Matplotlib.

**Features**

Fetches weather forecast data from OpenWeatherMap.

Processes and structures data into a Pandas DataFrame.

Converts date strings into a proper datetime format for plotting.

Generates a line plot showing temperature trends over time.

Creates a bar chart representing humidity levels.

Displays raw weather data in a tabular format for reference.


**Prerequisites**

Before running this script, ensure you have the following installed:

Python 3.x


**Required Python libraries:**

pip install requests pandas matplotlib


**Setup Instructions**

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


**Processing Data**

The JSON response is converted into a structured Pandas DataFrame, extracting relevant fields such as date, temperature, and humidity.

df = pd.DataFrame([{
    "Date": item["dt_txt"],
    "Temperature": item["main"]["temp"],
    "Humidity": item["main"]["humidity"]
} for item in data["list"]])


**Data Visualization**

The script generates two visualizations:

Temperature Trend: A line graph showing temperature variations over time.

Humidity Levels: A bar chart displaying humidity levels for the forecasted period.

plt.plot(df["Date"], df["Temperature"], marker="o", linestyle="-")
plt.bar(df["Date"], df["Humidity"], color="skyblue")


**Displaying Raw Data**

The processed DataFrame is printed in tabular format for reference.

print(df)



**Future Enhancements**

Add interactive visualizations using Plotly.

Implement a GUI for selecting cities dynamically.

Support multiple cities for comparison.

Store historical weather data for trend analysis.

**OUTPUT**
![Image](https://github.com/user-attachments/assets/790e032c-bf8a-4236-a595-ab472a373088)
![Image](https://github.com/user-attachments/assets/c5d24684-ef1b-4773-b7bd-4108f4e654a9)
