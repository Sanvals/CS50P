from plates import is_valid

def test_false():
    assert is_valid("CS05CS") == False
    assert is_valid("55050") == False
    assert is_valid("CS50CSPPP") == False
    assert is_valid("P") == False
    assert is_valid("PA!!") == False
    assert is_valid("PA55AA") == False
    assert is_valid("0ASA") == False
    assert is_valid("CS50P") == False
    assert is_valid("CS05") == False
    assert is_valid("PI.34") == False

def test_true():
    assert is_valid("CS51") == True
    assert is_valid("ALPHA1") == True
    assert is_valid("TRAN50") == True
    assert is_valid("AA") == True
    assert is_valid("AA5050") == True
