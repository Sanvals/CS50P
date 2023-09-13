import pytest
from seasons import calculate

def test_convert():
    with pytest.raises(SystemExit):
        calculate("1989-0209")