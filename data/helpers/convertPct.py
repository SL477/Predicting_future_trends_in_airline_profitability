def convertPct(x: str) -> int:
    """This is to remove the % from the dataframe and convert to an integer

    Parameters
    ----------
    x:str : string such as 7%

    Returns
    -------
    Integer or None
    """
    try:
        if len(x) > 1:
            return int(x[:-1])
    except:
        return None
    return None
