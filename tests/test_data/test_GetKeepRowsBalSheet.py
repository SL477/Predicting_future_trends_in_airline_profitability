from data.getKeepRowsBalSheet import getKeepRowsBalSheet


def test_getKeepRowsBalSheet():
    assert isinstance(getKeepRowsBalSheet(), list)
