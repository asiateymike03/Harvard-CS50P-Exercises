from numb3rs import validate

def test_validate():
    assert validate("127.0.0.1") == True

def test_validate():
    assert validate("cat") == False

def test_validate():
    assert validate("Frog") == False

def test_validate():
    assert validate("1.2.3.4") == True

def test_validate():
    assert validate("255.255.255.255") == True