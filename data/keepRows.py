import os


def getKeepRows() -> list:
    """gets the data in keeprows.txt as an array

    Returns
    -------
    A list
    """
    ret = []
    with open(os.path.join("data", "keeprows.txt")) as f:
        ret = [line.strip() for line in f.readlines()]
    return ret


if __name__ == '__main__':
    print(getKeepRows())
