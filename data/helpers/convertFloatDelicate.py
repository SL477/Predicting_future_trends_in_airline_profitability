def convertFloatDelicate(x: str) -> float:
    """This takes in a string and returns a float and doesn't raise an error

    Parameters
    ----------
    x:str : A string of the sort 3.2

    Returns
    -------
    Float or None
    """
    try:
        return float(x)
    except:
        return None
