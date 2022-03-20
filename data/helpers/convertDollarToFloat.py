def convertDollarToFloat(x: str) -> float:
    """This takes in the string '$ number' and spits out the number

    Parameters
    ----------
    x:str : takes in a string of the type $ 3.2

    Returns
    -------
    A float
    """
    try:
        return float(x[2:])
    except:
        return None
