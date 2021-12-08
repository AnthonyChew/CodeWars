import math


def format_duration(seconds):
    # your code here

    min = 60
    hour = 60 * min
    day = 24 * hour
    year = 365 * day

    result = {}
    count = 0

    timeLeft = seconds

    if((timeLeft / year) >= 1):

        # if year is > 1 add S at the end
        if(math.floor(timeLeft / year) > 1):
            result["years"] = math.floor(timeLeft / year)
        else:
            result["year"] = math.floor(timeLeft / year)

        timeLeft = timeLeft % year

    if((timeLeft / day) >= 1):

        if(math.floor(timeLeft / day) > 1):
            result["days"] = math.floor(timeLeft / day)
        else:
            result["day"] = math.floor(timeLeft / day)

        timeLeft = timeLeft % day

    if((timeLeft / hour) >= 1):

        if(math.floor(timeLeft / hour) > 1):
            result["hours"] = math.floor(timeLeft / hour)
        else:
            result["hour"] = math.floor(timeLeft / hour)

        timeLeft = timeLeft % hour

    if((timeLeft / min) >= 1):

        if(math.floor(timeLeft / min) > 1):
            result["minutes"] = math.floor(timeLeft / min)
        else:
            result["minute"] = math.floor(timeLeft / min)

        timeLeft = timeLeft % min

    if(timeLeft > 1):
        result["seconds"] = timeLeft
    else:
        if(timeLeft != 0):
            result["second"] = timeLeft

    resultString = ""
    resultLen = len(result) - 1

    for key, value in result.items():
        if(resultLen > 1):
            resultString += f"{value} {key}, "
        elif(resultLen == 1):
            resultString += f"{value} {key} and "
        else:
            resultString += f"{value} {key}"
        resultLen -= 1

    if(resultString == ""):
        resultString = "now"

    print(resultString)


format_duration(3602)
