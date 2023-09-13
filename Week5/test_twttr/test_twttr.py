from twttr import shorten

def test_word():
    assert shorten("hello word") == "hll wrd"
    assert shorten("HELLUVA") == "HLLV"
    assert shorten("Punc.tuation!") == "Pnc.ttn!"
    assert shorten("Ommite n1mb3rs") == "mmt n1mb3rs"