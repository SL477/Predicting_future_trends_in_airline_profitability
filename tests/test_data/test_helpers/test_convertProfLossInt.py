from data.helpers.convertProfLossInt import convertProfLossInt


def test_convertProfLossIntProf():
    assert convertProfLossInt('1,381') == 1381


def test_convertProfLossIntLoss():
    assert convertProfLossInt('(1,381)') == -1381


def test_convertProfLossIntNil():
    assert convertProfLossInt('-') == 0
