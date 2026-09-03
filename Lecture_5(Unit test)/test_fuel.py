import pytest
from fuel import convert, gauge

def test_convert_numbers():
    assert convert("2/4") == 50
    assert convert("3/4") == 75
    

def test_convert_errors():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")

    with pytest.raises(ValueError):
        convert("cat/cat")

def test_percentage():
    assert gauge(1) == "E"
    assert gauge(99) == 'F'
    assert gauge(50) == "50%"
