from data.helpers.convertFloatDelicate import convertFloatDelicate


def test_convertFloatDelicate():
    assert convertFloatDelicate('13.1') == 13.1


def test_convertFloatDelicateBad():
    assert convertFloatDelicate('no') is None
