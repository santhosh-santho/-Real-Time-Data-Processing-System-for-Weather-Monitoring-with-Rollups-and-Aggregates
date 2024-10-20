import requests
import time
import pandas as pd
from .config import API_KEY, CITIES, UPDATE_INTERVAL

def fetch_weather_data():
    data = []
    for city_id in CITIES:
        url = f"https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            data.append(response.json())
        else:
            print(f"Failed to fetch data for city ID {city_id}")
    df = pd.DataFrame(data)
    df.to_csv("data/weather_data.csv", index=False)

def main():
    while True:
        fetch_weather_data()
        time.sleep(UPDATE_INTERVAL)

if __name__ == "__main__":
    main()