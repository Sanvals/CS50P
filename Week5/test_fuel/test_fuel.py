from fuel import convert, gauge
import pytest

def test_convert():
    with pytest.raises(ValueError):
        assert convert("cat/dog")
    with pytest.raises(ValueError):
        assert convert("8/4")
    with pytest.raises(ZeroDivisionError):
        assert convert("7/0")
    assert convert("2/3") == 67

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(2) == "2%"
    assert gauge(30) == "30%"
    assert gauge(45) == "45%"
    assert gauge(98) == "98%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
