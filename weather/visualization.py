import pandas as pd
import matplotlib.pyplot as plt

def plot_temperature_trend(df):
    plt.plot(df['date'], df['temp'])
    plt.xlabel('Date')
    plt.ylabel('Temperature (Celsius)')
    plt.show()

# ... other visualization functions