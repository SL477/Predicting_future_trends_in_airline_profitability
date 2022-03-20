import pandas as pd


def getAirline(row: pd.Series) -> str:
    """Run through the potential columns and return the one that matches

    Parameters
    ----------
    row:pd.Series : row series of dataframe with Airline run through get
    dummies

    Returns
    -------
    string of the airline
    """
    ret = ''

    for c in ['AirTran', 'Alaska', 'Allegiant', 'AmericaWest', 'American', 'Continental', 'Delta', 'Frontier', 'Hawaiian', 'Northwest', 'Southwest', 'Spirit', 'US Airways', 'United', 'VirginAmerica', 'jetBlue']:
        if row[c]:
            ret = c
            break

    return ret


def get_airline_from_dummies(df: pd.DataFrame) -> pd.Series:
    """This is to reverse the effect of the get dummies call on the dataframe

    Parameters
    ----------
    df:pd.DataFrame : dataframe with the Airline column run 
    through Panda's get dummies

    Returns
    -------
    pandas series of airline labels
    """
    ret = df.apply(lambda row: getAirline(row), axis=1)
    return ret
