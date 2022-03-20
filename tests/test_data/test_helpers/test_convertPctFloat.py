from data.helpers.convertPctFloat import convertPctFloat


def testPctFloatStand():
    assert convertPctFloat('13.1%') == 13.1


def testPctFloatBad():
    assert convertPctFloat(1) is None
