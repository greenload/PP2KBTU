import datetime as dt

#Write a Python program to subtract five days from current date.
def minus_five():
    today = dt.date.today()
    deltaFive = dt.timedelta(days=5)
    fiveDaysBefore = today - deltaFive
    return fiveDaysBefore

#Write a Python program to print yesterday, today, tomorrow.
def yetoto():
    today = dt.date.today()
    deltaOne =  dt.timedelta(days=1)
    yesterday = today - deltaOne
    tomorrow = today + deltaOne

    print(f"Today is: {today}.\nTomorrow will be: {tomorrow}.\nYesterday was: {yesterday}.\n")
    
#Write a Python program to drop microseconds from datetime.
def mic_drop():
    notPrecizedTime = dt.datetime.now().replace(microsecond=0)
    return notPrecizedTime
    
#Write a Python program to calculate two date difference in seconds.
def two_diff(firstDate, secondDate):
    dateDifference = dt.timedelta.total_seconds(firstDate - secondDate)
    return dateDifference