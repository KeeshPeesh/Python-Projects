import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Projects\\KFrangos_WeatherApplication\\WeatherStationData.csv')

temp_high = df['Temperature Highest'].to_numpy()
temp_low = df['Temperature Lowest'].to_numpy()
humidity = df['Humidity (%)'].to_numpy()
wind = df['Wind in mph'].to_numpy()

print("Weather Station Data Analysis")
choice = input("Menu:" \
"\n 1 to view all data," \
"\n 2 to view first five rows," \
"\n 3 to view statistics," \
"\n 4 to visualize data," \
"\n 5 to add new station," \
"\n 6 to update existing station," \
"\n 7 to exit "
"\nEnter your choice: ")

if choice == '1':
  print("-----> File Information : ALL ")
  print(df.info())

if choice == '2':
  print("-----> First Information : First five rows ")
  print(df.head(5))

if choice == '3':
  df["Date"] = pd.to_datetime(df["Date"])
  print(f"Temperature Highest : {temp_high}")
  print(f"Temperature Lowest : {temp_low}")
  print(f"Humidity : {humidity}")
  print(f"Wind : {wind}")

  if 'Humidity (%)' in df.columns:
      if df ['Humidity (%)'].isnull().all():
        humidity = [0] * len(df)
      else:
        humidity = df['Humidity (%)'].fillna(0).to_numpy()
  else:
      print("Column 'Humidity (%)' not found!")
      humidity = [0] * len(df)
      humidity = None

if choice == '4':
  #VISUALIZATION
  plt.plot(df['Date'], temp_high, label = 'High Temp', marker = "o")
  plt.plot(df['Date'], temp_low, label = 'Low Temp', marker = "x")

  plt.title("Daily Temperature Overview")
  plt.xlabel("Date")
  plt.ylabel("Temperature (F)")
  plt.legend()
  plt.grid(True)
  plt.show()

  #BAR CHART
  plt.bar(df['Location'], wind, color = 'skyblue')
  plt.title("Wind Speed by Location")
  plt.xlabel("Location")
  plt.ylabel("Wind (mph)")
  plt.show()

  #SCATTER PLOT
  plt.scatter(temp_high, humidity, color="green")
  plt.title("Humidity vs High Temperature")
  plt.xlabel("Temperature (F)")
  plt.ylabel("Humidity (%)")
  plt.show()

if choice == '5':

# ✔ Load CSV data with original rows and columns
# ✔ Allow users to add a new weather station with complete data for a different city
# ✔ Allow users to update information from existing weather stations
# ✔ Validate user input (correct date format, numeric data for temperature, humidity, wind)
# ✔ Append user-provided data to the CSV
# ✔ Calculate updated statistics for all stations
# ✔ Update visualizations to reflect new rows, new stations, and user-entered or updated data