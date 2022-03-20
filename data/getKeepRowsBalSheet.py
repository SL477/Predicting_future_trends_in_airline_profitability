import os


def getKeepRowsBalSheet() -> list:
    """gets the data in keepRowsBalSheet.txt as an array

    Returns
    -------
    A list
    """
    ret = []
    with open(os.path.join("data", "keepRowsBalSheet.txt")) as f:
        ret = [line.strip() for line in f.readlines()]
    return ret
