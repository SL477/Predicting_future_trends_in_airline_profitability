from data.helpers.convertPct import convertPct


def test_normal():
    assert convertPct('13%') == 13


def test_other():
    assert convertPct('nan') is None
