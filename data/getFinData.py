"""This is to download the finance data and save it to CSV"""
# Imports
import pandas as pd
from getKeepRowsBalSheet import getKeepRowsBalSheet
from helpers.convertProfLossInt import convertProfLossInt

balData = [
    'http://web.mit.edu/airlinedata/www/2019%2012%20Month%20Documents/Profitability,%20Balance%20Sheet%20&%20Cash%20Flow/Income%20Statement/Operating%20Income%20(Loss).htm',
    'http://web.mit.edu/airlinedata/www/2019%2012%20Month%20Documents/Profitability,%20Balance%20Sheet%20&%20Cash%20Flow/Income%20Statement/Pretax%20Income%20(Loss).htm',
    'http://web.mit.edu/airlinedata/www/2019%2012%20Month%20Documents/Profitability,%20Balance%20Sheet%20&%20Cash%20Flow/Income%20Statement/Net%20Income%20(Loss).htm',
    'http://web.mit.edu/airlinedata/www/2019%2012%20Month%20Documents/Profitability,%20Balance%20Sheet%20&%20Cash%20Flow/Income%20Statement/Regional%20Affiliate%20Revenue.htm',
    'http://web.mit.edu/airlinedata/www/2019%2012%20Month%20Documents/Profitability,%20Balance%20Sheet%20&%20Cash%20Flow/SEC%20Balance%20Sheet/Cash%20and%20Short-term%20Investments.htm',
    'http://web.mit.edu/airlinedata/www/2019%2012%20Month%20Documents/Profitability,%20Balance%20Sheet%20&%20Cash%20Flow/SEC%20Balance%20Sheet/Restricted%20Cash%20and%20Short-term%20Investments.htm',
    'http://web.mit.edu/airlinedata/www/2019%2012%20Month%20Documents/Profitability,%20Balance%20Sheet%20&%20Cash%20Flow/SEC%20Balance%20Sheet/Long-term%20Debt%20&%20Capital%20Lease%20Obligations,%20Less%20Current%20Maturities.htm',
    'http://web.mit.edu/airlinedata/www/2019%2012%20Month%20Documents/Profitability,%20Balance%20Sheet%20&%20Cash%20Flow/SEC%20Balance%20Sheet/Pension%20and%20Post%20Retirement%20Benefits.htm',
    'http://web.mit.edu/airlinedata/www/2019%2012%20Month%20Documents/Profitability,%20Balance%20Sheet%20&%20Cash%20Flow/Cash%20Flow%20Statement/Net%20Cash%20Provided%20by%20(Used%20in)%20Operating%20Activity.htm',
    'http://web.mit.edu/airlinedata/www/2019%2012%20Month%20Documents/Profitability,%20Balance%20Sheet%20&%20Cash%20Flow/Cash%20Flow%20Statement/Net%20Cash%20Provided%20by%20(Used%20in)%20Investing%20Activities.htm',
    'http://web.mit.edu/airlinedata/www/2019%2012%20Month%20Documents/Profitability,%20Balance%20Sheet%20&%20Cash%20Flow/Cash%20Flow%20Statement/Net%20Cash%20Provided%20by%20(Used%20in)%20Financing%20Activities.htm',
    'http://web.mit.edu/airlinedata/www/2019%2012%20Month%20Documents/Profitability,%20Balance%20Sheet%20&%20Cash%20Flow/Cash%20Flow%20Statement/Payments%20on%20Long-term%20Debt%20and%20Capital%20Lease%20Obligations.htm',
    'http://web.mit.edu/airlinedata/www/2019%2012%20Month%20Documents/Profitability,%20Balance%20Sheet%20&%20Cash%20Flow/Cash%20Flow%20Statement/Proceeds%20from%20Issuance%20of%20Long-term%20Debt.htm',
    'http://web.mit.edu/airlinedata/www/2019%2012%20Month%20Documents/Profitability,%20Balance%20Sheet%20&%20Cash%20Flow/Cash%20Flow%20Statement/Net%20Increase%20(Decrease)%20in%20Cash.htm'
]

keeprows = getKeepRowsBalSheet()


def sortOutBalSheet(t: pd.DataFrame) -> pd.DataFrame:
    """Bins the rubbish rows and columns. Converts to Int and unpivots the data

    Parameters
    ----------
    t:pd.DataFrame : Pandas dataframe retrieved from the website


    Returns
    -------
    Pandas dataframe
    """
    df = t.copy()
    # Get the title of the row
    title = ''
    newCols = [str(x) for x in range(2000, 2020)]
    newCols = ['Airline', 'bin'] + newCols
    df.columns = newCols
    for cell in df['Airline'].tolist():
        if not isinstance(cell, str):
            break
        if title == '':
            title = str(cell)
        else:
            title += ' ' + str(cell)
    # print(title)

    # Drop junk
    df.set_index('Airline', inplace=True)
    df = df[df.index.isin(keeprows)]
    df.reset_index(inplace=True)

    # Drop extra column
    df.drop('bin', axis=1, inplace=True)

    # Unpivot
    df = pd.melt(df, id_vars=['Airline'])

    # Rename cols
    df.columns = ['Airline', 'Year', title]

    # Sort out data type
    df[title] = df[title].apply(convertProfLossInt)

    # Replace sprint so that it is consistant
    df['Airline'] = df['Airline'].replace({
        'Spirit Airlines Inc': 'Spirit Airlines, Inc.',
        'Spirit Airlines, Inc': 'Spirit Airlines, Inc.'
    })

    return df

# Build the combined dataframe


def getFinancialData() -> pd.DataFrame:
    """This gets the combined dataframe for the financial data
    Returns
    -------
    Pandas Dataframe"""
    ret = None
    for lnk in balData:
        tmp = sortOutBalSheet(pd.read_html(lnk)[0])
        if ret is None:
            ret = tmp
        else:
            ret = ret.merge(tmp, on=['Airline', 'Year'], how='left')
    return ret


if __name__ == '__main__':
    df = getFinancialData()
    df.to_csv('airlineFinData.csv')
    print(df.head())
