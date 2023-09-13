from bank import value


def test_20():
    assert value("he") == 20
    assert value("hilco") == 20
    assert value("hocho") == 20


def test_100():
    assert value("olita") == 100
    assert value("enulco") == 100
    assert value("ayayay") == 100


def test_0():
    assert value("hello") == 0
    assert value("Hello") == 0