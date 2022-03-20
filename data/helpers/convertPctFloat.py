def convertPctFloat(x: str) -> int:
    """This is to remove the % from the dataframe and convert to an float

    Parameters
    ----------
    x:str : a string such as 3.2%

    Returns
    -------
    int or None
    """
    try:
        if len(x) > 1:
            return float(x[:-1])
    except:
        return None
    return None
