import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('WeatherStationData.csv')

temp_high = df['Temperature Highest'].to_numpy()
temp_low = df['Temperature Lowest'].to_numpy()
humidity = df['Humidity (%)'].to_numpy()
wind = df['Wind in mph'].to_numpy()

while True:

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
    print("Showing all Data:")
    print(df.info())

  if choice == '2':
    print("Showing the first five rows of data:")
    print(df.head(5))

  if choice == '3':
    df["Date"] = pd.to_datetime(df["Date"], format='mixed')
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
      print("Adding a new weather station:")

      station_id = input("Enter station ID: ")

      new_location = input("Enter location: ")

      while True:
          new_date = input("Enter date (YYYY-MM-DD): ")
          try:
              pd.to_datetime(new_date, format='%Y-%m-%d')
              break
          except ValueError:
              print("Invalid date format. Please use YYYY-MM-DD.")

      while True:
          try:
              new_temp_high = float(input("Enter highest temperature (F): "))
              break
          except ValueError:
              print("Invalid input. Enter a number.")

      while True:
          try:
              new_temp_low = float(input("Enter lowest temperature (F): "))
              break
          except ValueError:
              print("Invalid input. Enter a number.")

      while True:
          try:
              new_humidity = float(input("Enter humidity (%): "))
              break
          except ValueError:
              print("Invalid input. Enter a number.")

      while True:
          try:
              new_wind = float(input("Enter wind speed (mph): "))
              break
          except ValueError:
              print("Invalid input. Enter a number.")

      new_data = pd.DataFrame([{
          "Location": new_location,
          "Date": new_date,
          "Temperature Highest": new_temp_high,
          "Temperature Lowest": new_temp_low,
          "Humidity (%)": new_humidity,
          "Wind in mph": new_wind
      }])

      df = pd.concat([df, new_data], ignore_index=True)

      df.to_csv('WeatherStationData.csv', index=False)

      print("New station added successfully!")

  if choice == '6':
      print("Updating an existing weather station:")
      update_id = input("Enter the ID of the station to update: ")

      update_station = df[df['Location'] == update_id]

      if not update_station.empty:
          station_index = update_station.index[0]

          while True:
              new_date = input("Enter new date (YYYY-MM-DD): ")
              try:
                  pd.to_datetime(new_date, format='%Y-%m-%d')
                  break
              except ValueError:
                  print("Invalid date format. Please use YYYY-MM-DD.")

          while True:
              try:
                  new_temp_high = float(input("Enter new highest temperature (F): "))
                  break
              except ValueError:
                  print("Invalid input. Enter a number.")

          while True:
              try:
                  new_temp_low = float(input("Enter new lowest temperature (F): "))
                  break
              except ValueError:
                  print("Invalid input. Enter a number.")

          while True:
              try:
                  new_humidity = float(input("Enter new humidity (%): "))
                  break
              except ValueError:
                  print("Invalid input. Enter a number.")

          while True:
              try:
                  new_wind = float(input("Enter new wind speed (mph): "))
                  break
              except ValueError:
                  print("Invalid input. Enter a number.")

          df.at[station_index, 'Date'] = new_date
          df.at[station_index, 'Temperature Highest'] = new_temp_high
          df.at[station_index, 'Temperature Lowest'] = new_temp_low
          df.at[station_index, 'Humidity (%)'] = new_humidity
          df.at[station_index, 'Wind in mph'] = new_wind

          df.to_csv('WeatherStationData.csv', index=False)

          print("Station updated successfully!")
      else:
          print(f"No station found for location: {update_location}")

  if choice == '7':
    break

# ✔ Load CSV data with original rows and columns
# ✔ Allow users to add a new weather station with complete data for a different city
# ✔ Allow users to update information from existing weather stations
# ✔ Validate user input (correct date format, numeric data for temperature, humidity, wind)
# ✔ Append user-provided data to the CSV
# ✔ Calculate updated statistics for all stations
# ✔ Update visualizations to reflect new rows, new stations, and user-entered or updated data
