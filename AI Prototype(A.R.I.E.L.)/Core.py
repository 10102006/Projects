"""
STATUS: Working

OVERVIEW: Can implement function of [notification] and [speaker] and perform some calculation

IMPROVEMENTS:
    - TODO Document
    - Follow the [README]

"""

# @ Imports
import speaker
import notification
from time import localtime
from datetime import datetime

# * Defining
currentTime = localtime().tm_hour
todays = datetime.today()


def Greet(name="Master"):

    # Finding the correct greeting
    if currentTime < 12 and currentTime > 0:
        time_period = "morning"
    elif currentTime < 18 and currentTime > 12:
        time_period = "afternoon"
    else:
        time_period = "evening"

    # Formulating the greeting
    greeting = f"Good {time_period}, {name}. Today is {todays.date()}, and time is {todays.time().hour} hours."

    # Initialising commands
    speaker.Speak(greeting)
    notification.Notify("Have a Good Day!")


# ? Implementation
if __name__ == "__main__":
    Greet("Udit")
