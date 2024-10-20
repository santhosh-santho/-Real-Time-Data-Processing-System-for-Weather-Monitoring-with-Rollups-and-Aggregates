import pytest
from src.utils import convert_temp_to_celsius

def test_convert_temp_to_celsius():
    assert convert_temp_to_celsius(300) == 27