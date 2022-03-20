def convertProfLossInt(x: str) -> int:
    """This is to convert numbers such as (9,999) to something sensible like -9999

    Parameters
    ----------
    x:str : string such as (9,999)

    Returns
    -------
    int
    """
    x = x.replace(',', '')
    if x == '-':
        return 0
    elif x.startswith('('):
        x = x[1:-1]
        return int(x) * -1
    return int(x)
