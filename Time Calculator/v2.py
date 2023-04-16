# DOCUMENT.

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

    datetime_time = (time + elapsedtime)
    noOfDays = (datetime_time.day - time.day)
    str_time = datetime_time.strftime(r'%I:%M %p')

    noOfDaysPrompt = ''
    weekdayPromt = ''

    if day:
        weekdayPromt = f", {days[(day + datetime_time.day - time.day)%7]}"
    if noOfDays == 1:
        noOfDaysPrompt = f" (next day)"
    elif noOfDays:
        noOfDaysPrompt = f" ({noOfDays} days later)"

    print(f"{str_time}{weekdayPromt}{noOfDaysPrompt}")


# ? Implementation
if __name__ == "__main__":
    add_time("11:43 AM", "40:20")
