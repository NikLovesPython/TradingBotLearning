from data import *


def get_trend(df):
    trends = {}
    i = 0
    j = 1

    while j < len(df):
        if "4" in inpereter(i, j, df):
            print("Error inpereting data")
        else:
            trends["{}-{}".format(df.index.tolist()[i], df.index.tolist()[j])
                   ] = inpereter(i, j, df)
        i += 1
        j += 1

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

    result = {}
    trend = []

    # getting trend
    trend.append(helper_inpereter(pervious_open, pervious_close))
    trend.append(helper_inpereter(pervious_close, open))
    trend.append(helper_inpereter(open, close))
    result["trend"] = trend

    var = {open: "open", close: "close", pervious_open: "pervious_open",
           pervious_close: "pervious_close"}

    # getting max and min values
    maximum = max(var)
    result["maximum"] = (var.get(maximum), maximum)

    # getting min value
    minimum = min(var)
    result["minimum"] = (var.get(minimum), minimum)

    # print("open: ", open)
    # print("close: ", close)
    # print("pervious_open: ", pervious_open)
    # print("pervious_close: ", pervious_close)
    # print("result:", result)

    return result


def helper_inpereter(i, j):
    if i < j:
        return 1
    elif i > j:
        return 0
    elif i == j:
        return 3


data = get_trend(dataF)
print(data["{}-{}".format(dataF.index.tolist()[0], dataF.index.tolist()[1])])
print(dataF)
