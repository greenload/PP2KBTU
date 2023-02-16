import datelab
import datetime

print(f"{datelab.minus_five()} was exactly five days ago.\n")

datelab.yetoto()

print(f"{datelab.mic_drop()} - is current date and time without microseconds.\n")

firstDate = datetime.date.today()
secondDate = datelab.minus_five()

datesDifference = datelab.two_diff(firstDate, secondDate)

print(f"Difference between two dates is: {datesDifference} seconds.\n")