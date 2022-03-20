import re


def convertDollarToIntWithSpace(x: str) -> float:
    """Get rid of extra spaces after the dollar sign and bin the comma

    Parameters
    ----------
    x:str : takes in a string of the sort $  1,000

    Returns
    -------
    Integer value
    """
    try:
        num = re.search("(\d*,\d*)", x)
        if num is None:
            num = re.search("\d+", x).group(0)
        else:
            # need to ditch the comma
            num = num.group(0)
            n = [i for i in list(num) if i != ',']
            num = ''.join(n)
        return int(num)
    except:
        return None
