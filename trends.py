from data import *


def get_trend(df):
    trends = {}
    i = 0
    j = 1

    while j < df.index:
        if "4" in inpereter(i, j, df):
            print("Error inpereting data")
        else:
            trends["{}-{}".format(df.Date.iloc[i], df.Date.iloc[j])
                   ]["trend"] = inpereter(i, j, df)

    return trends


def inpereter(i, j, df):
    """
    returns a string with three characters each 
    character respresents rise, decline or stability
    """
    open = df.Open.iloc[j]
    close = df.Close.iloc[j]
    pervious_open = df.Open.iloc[i]
    pervious_close = df.Close.iloc[i]

    result = [4, 4, 4]

    result[0] = helper_inpereter(pervious_open, pervious_close)
    result[1] = helper_inpereter(pervious_close, open)
    result[2] = helper_inpereter(open, close)

    return result


def helper_inpereter(i, j):
    if i < j:
        return 1
    elif i > j:
        return 0
    elif i == j:
        return 3


print(get_trend(dataF))
