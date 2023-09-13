import pytest
from working import convert


def test_convert():
    assert convert("9 AM to 9 PM") == "09:00 to 21:00"
    assert convert("9:00 AM to 9:00 PM") == "09:00 to 21:00"

    with pytest.raises(ValueError):
        convert("9 AM - 9 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 9:60 PM")