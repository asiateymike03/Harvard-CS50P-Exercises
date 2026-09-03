from seasons import validate_birthday
import pytest

def test_season():
    assert validate_birthday("2025-08-17") == "Five hundred twenty-five thousand, six hundred minutes"
    assert validate_birthday("2024-08-17") == "One million, fifty-one thousand, two hundred minutes"

def test_season():
    with pytest.raises(ValueError):
        validate_birthday("January 1, 2004")
    