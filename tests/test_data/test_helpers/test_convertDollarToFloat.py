from data.helpers.convertDollarToFloat import convertDollarToFloat


def test_convert_Dollar_To_Float_Standard():
    assert convertDollarToFloat("$ 15.61") == 15.61


def test_convert_Dollar_To_Float_Bad():
    assert convertDollarToFloat("$ -") is None
