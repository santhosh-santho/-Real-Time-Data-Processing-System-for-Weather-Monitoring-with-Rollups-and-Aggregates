import pandas as pd
from .utils import convert_temp_to_celsius

def process_weather_data():
    df = pd.read_csv("data/weather_data.csv")
    df['temp'] = convert_temp_to_celsius(df['temp'])
    # ... other processing steps
    df.to_csv("data/daily_summaries.csv", index=False)