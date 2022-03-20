from data.getFlightDataSettings import getFlightDataSettings
import pandas as pd


def test_getFlightDataSettings():
    assert isinstance(getFlightDataSettings(), pd.DataFrame)
