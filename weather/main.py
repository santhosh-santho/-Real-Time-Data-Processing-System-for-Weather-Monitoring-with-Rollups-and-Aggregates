from .data_acquisition import main as fetch_data
from .data_processing import process_weather_data
from .visualization import plot_temperature_trend
from .config import VISUALIZATION_INTERVAL

def main():
    while True:
        fetch_data()
        process_weather_data()
        plot_temperature_trend()  # Replace with your desired visualization
        time.sleep(VISUALIZATION_INTERVAL)

if __name__ == "__main__":
    main()