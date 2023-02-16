import datetime

#Write a Python program to subtract five days from current date.
def minus_five():
    today = datetime.date.today()
    deltaFive = datetime.timedelta(days=5)
    fiveDaysBefore = today - deltaFive
    return fiveDaysBefore

#Write a Python program to print yesterday, today, tomorrow.
def yetoto():
    today = datetime.date.today()
    deltaOne =  datetime.timedelta(days=1)
    yesterday = today - deltaOne
    tomorrow = today + deltaOne

    print(f"Today is: {today}.\nTomorrow will be: {tomorrow}.\nYesterday was: {yesterday}.\n")
    
#Write a Python program to drop microseconds from datetime.
def mic_drop():
    notPrecizedTime = datetime.datetime.now().replace(microsecond=0)
    return notPrecizedTime
    
#Write a Python program to calculate two date difference in seconds.
def two_diff(firstDate, secondDate):
    dateDifference = firstDate - secondDate
    return dateDifference