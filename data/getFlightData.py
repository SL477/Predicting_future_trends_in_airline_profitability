"""This is to retrieve all of the data, minus the financial data section, from MIT's site and save it to CSV"""

# Imports
import pandas as pd
from getFlightDataSettings import getFlightDataSettings
from helpers import convertPct, convertPctFloat, convertDollarToFloat, convertFloatDelicate, convertDollarToIntWithSpace
from keepRows import getKeepRows

keeprows = getKeepRows()


def sortOutDataFrame(orgDf: pd.DataFrame, newColName: str, convertOutputFn: callable, doNotDelete2ndCol=True) -> pd.DataFrame:
    """This takes in the original dataframe, bins the rubbish rows and columns. Converts the data. Unpivots and returns the dataframe

    Parameters
    ----------
    orgDf:pd.DataFrame : Original dataframe from MIT

    newColName:str : The name of the target column

    convertOutputFn:callable : how to unravel the string with the number into a number

    doNotDelete2ndCol :
         (Default value = True) if this is true the second column of the returned dataset won't be deleted. This is because of the formating of MIT's site where sometimes there is a phantom column to get rid of

    Returns
    -------
    Pandas Dataframe
    """
    retDF = orgDf[0].copy()
    colNames = [str(x) for x in range(1995, 2020)]

    if doNotDelete2ndCol:
        colNames = ['Airline'] + colNames
        retDF.columns = colNames
    else:
        colNames = ['Airline', 'bin'] + colNames
        retDF.columns = colNames
        retDF.drop('bin', inplace=True, axis=1)  # Throw away useless column

    retDF.dropna(inplace=True, subset=['Airline'])  # Wipe out the useless rows
    # rowsToDrop = ['$ Billions', '--sub Network', '-- sub LCC', '-- sub Other', 'Total All Sectors', 'Total Industry', 'Data  Source: US DOT Form 41 via BTS,  Schedule P12.']
    # for r in removerows:
    #    rowsToDrop.append(r)
    retDF.set_index('Airline', inplace=True)
    # retDF = retDF[~retDF.index.isin(rowsToDrop)] # https://stackoverflow.com/questions/19960077/how-to-filter-pandas-dataframe-using-in-and-not-in-like-in-sql
    retDF = retDF[retDF.index.isin(keeprows)]

    # Need to unpivot the columns
    retDF.reset_index(inplace=True)
    retDF = pd.melt(retDF, id_vars=['Airline'])
    # Relabel columns
    retDF.columns = ['Airline', 'Year', newColName]

    # Sort out data-types
    retDF['Year'] = retDF['Year'].apply(int)
    retDF[newColName] = retDF[newColName].apply(convertOutputFn)
    return retDF


def getFlightData() -> pd.DataFrame:
    """This is to get the pandas dataframe of the flights data
    Returns
    -------
    Pandas dataframe"""
    ret = None
    settingsDf = getFlightDataSettings()
    for row in settingsDf.itertuples():
        # df = sortOutDataFrame(pd.read_html())
        if row.Function == 'convertDollarToFloat':
            fn = convertDollarToFloat
        elif row.Function == 'convertFloatDelicate':
            fn = convertFloatDelicate
        elif row.Function == 'convertDollarToIntWithSpace':
            fn = convertDollarToIntWithSpace
        elif row.Function == 'convertPct':
            fn = convertPct
        else:
            fn = convertPctFloat

        df = sortOutDataFrame(pd.read_html(row.WebAddress), row.NewColTitle, fn, doNotDelete2ndCol=row.DeleteSecondCol)

        if ret is None:
            ret = df
        else:
            ret = ret.merge(df, on=['Airline', 'Year'], how='left')
            # some of the employment data is missing for America West

    return ret


if __name__ == '__main__':
    df = getFlightData()
    print(df.head())
    df.to_csv("airlineData.csv")
