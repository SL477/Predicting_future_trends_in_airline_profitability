import pandas as pd
import os


def getFlightDataSettings() -> pd.DataFrame:
    """This is to get the dataframe of the settings

    Returns
    -------
    Pandas dataframe
    """
    df = pd.read_excel(os.path.join(
        "data",
        "flightDataImportSettings.xlsx"
    ), sheet_name="flightDataImportSettings")
    # Trim any leading spaces
    for col in ['WebAddress', 'NewColTitle', 'Function', 'Section', 'Subsection', 'DataType']:
        df[col] = df[col].str.strip()
    df['DeleteSecondCol'] = df['DeleteSecondCol'].astype('bool')
    return df


if __name__ == "__main__":
    print(getFlightDataSettings().head())
