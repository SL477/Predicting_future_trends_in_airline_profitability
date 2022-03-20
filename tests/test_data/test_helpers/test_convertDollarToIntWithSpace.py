from data.helpers.convertDollarToIntWithSpace import convertDollarToIntWithSpace


def test_convertDollarToIntWithSpaceNorm():
    assert convertDollarToIntWithSpace('$     10,677') == 10677


def test_convertDollarToIntWithSpaceBad():
    assert convertDollarToIntWithSpace('$         47') == 47


def test_convertDollarToIntWithSpaceReallyBad():
    assert convertDollarToIntWithSpace('$         -') is None
