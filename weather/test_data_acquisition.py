import pytest
from src.data_acquisition import fetch_weather_data

def test_fetch_weather_data():
    data = fetch_weather_data()
    assert len(data) > 0
    assert 'main' in data[0]
    assert 'temp' in data[0]