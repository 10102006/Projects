"""
STATUS: Working

OVERVIEW: Uses [plyer] module to show a notification

IMPROVEMENTS:
    - Learn about how to add more widgets in the notification
    TODO add text box

"""

# @ Imports
from plyer import notification
from os import path, getcwd


# * Defining

icon = path.join(getcwd(), "icon.ico")

def Notify(message):
    """
    Basic notifcation making function
    """
    notification.notify(
        title="ARIEL(1.1)",
        message=message,
        app_icon=icon,
        timeout=10
    )


# ? Implementation
if __name__ == "__main__":
    Notify("Hello World!")
