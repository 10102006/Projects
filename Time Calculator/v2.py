"""
STATUS: Wokring

OVERVIEW: Better Time Calculator
"""

# @ Imports
import datetime
from datetime import timedelta, datetime

days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
# * Defining


def add_time(time, elapsedtime, day=''):
    elapsedtime = [int(char) for char in elapsedtime.split(':')]
    if day:
        day = days.index(day.capitalize())

    time = datetime.strptime(f'{time}', r'%I:%M %p')
    elapsedtime = timedelta(hours=elapsedtime[0], minutes=elapsedtime[1])

    newtime = (time + elapsedtime)
    noOfDays = (newtime.day - time.day)
    str_newtime = newtime.strftime(r'%I:%M %p')

    daysprompt = ''
    daypromt = ''

    if day:
        daypromt = f", {days[(day + newtime.day - time.day)%7]}"
    if noOfDays == 1:
        daysprompt = f" (next day)"
    elif noOfDays:
        daysprompt = f" ({noOfDays} days later)"

    print(f"{str_newtime}{daypromt}{daysprompt}")



# ? Implementation
if __name__ == "__main__":
    add_time("11:43 AM", "40:20")
