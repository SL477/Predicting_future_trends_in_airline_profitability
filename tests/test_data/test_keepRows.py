from data.keepRows import getKeepRows


def test_getKeepRows():
    assert isinstance(getKeepRows(), list)
