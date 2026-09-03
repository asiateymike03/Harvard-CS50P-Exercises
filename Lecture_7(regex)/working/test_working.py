from working import convert
import pytest

def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_convert():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_convert():
    assert convert("10:30 PM to 8 AM") == "22:30 to 8:00"

def test_convert():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_convert():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")