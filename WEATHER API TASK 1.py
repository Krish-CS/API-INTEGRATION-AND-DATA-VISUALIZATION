import requests
import pandas as pd
import matplotlib.pyplot as plt

API_KEY = "ed219ab042be2e7c364bffaa82077bce"
CITY = "India"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"


response = requests.get(URL)
data = response.json()

# Extracting relevant data         
df = pd.DataFrame([{
    "Date": item["dt_txt"],
    "Temperature": item["main"]["temp"],
    "Humidity": item["main"]["humidity"]
} for item in data["list"]])


df["Date"] = pd.to_datetime(df["Date"])

# Line plot for Temperature
plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Temperature"], marker="o", linestyle="-", label="Temperature (°C)")
plt.xticks(rotation=45)
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title(f"Temperature Trend in {CITY}")
plt.legend()
plt.grid(True)
plt.show()

# Bar plot for Humidity
plt.figure(figsize=(10, 5))
plt.bar(df["Date"], df["Humidity"], label="Humidity (%)", color="skyblue")
plt.xticks(rotation=45)
plt.xlabel("Date")
plt.ylabel("Humidity (%)")
plt.title(f"Humidity Levels in {CITY}")
plt.legend()
plt.grid(axis="y")
plt.show()

# Display raw data
print("\nRaw Weather Data:")
print(df)