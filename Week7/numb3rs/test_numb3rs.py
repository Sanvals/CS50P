from numb3rs import validate

def test_validate():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("8.8.8.8") == True
    assert validate("255.8.8.8") == True

    assert validate("255") == False
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.700") == False
    assert validate("cat") == False
    assert validate("512.1.1.1") == False