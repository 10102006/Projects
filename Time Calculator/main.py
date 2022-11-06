"""
STATUS:Working

OVERVIEW: DateTime Manipulators

IMPROVEMENTS:
    - TODO Document
    - Cleaner and StreamLined
    - More features
    - FIXME ErrorHandling
"""

# @ Imports
import calendar
import datetime
from datetime import datetime, timedelta

# * Defining


class TimeManipulator:
    def __init__(self, currtTime, timeDiff='', currtDay=''):
        """ So this functions makes a class a constructor """
        self.currentTime = currtTime
        self.timeDifference = timeDiff
        self.currentDay = currtDay.capitalize()

        self.Converter()
        self.Operations()

    def Converter(self):
        """Will convert the string into an object of datetime
        """
        self.currentDate = datetime.strptime(self.currentTime, r'%I:%M %p')

        # Calculating timedelta
        hourDiff, minDiff = self.timeDifference.split(':')
        self.timeDifference = timedelta(
            hours=int(hourDiff), minutes=int(minDiff))

        self.SetCalender()

    def SetCalender(self):
        """ """
        for i, day in enumerate(calendar.day_name):
            if day == self.currentDay:
                self.currentDay = int(i)

    def Operations(self):
        """ """
        self.futureDate = (self.currentDate +
                           self.timeDifference)
        futureTime = self.futureDate.strftime("%I:%M %p")
        concurrentDays = (self.futureDate.day - self.currentDate.day)
        futureDay = f", {calendar.day_name[concurrentDays % 7]}" if self.currentDay != '' else ''

        if concurrentDays == 1:
            print(f'{futureTime}{futureDay} (next day)')
        elif concurrentDays > 1:
            print(f'{futureTime}{futureDay} ({concurrentDays} days later)')
        else:
            print(f'{futureTime}{futureDay}')

    def Viewer(self):
        """ Main function
        datetime2 = datetime1 + timedelta
        """
        pass


# ? Implementation
if __name__ == "__main__":
    '''
        add_time("3:00 PM", "3:10")
        # Returns: 6:10 PM

        add_time("11:30 AM", "2:32", "Monday")
        # Returns: 2:02 PM, Monday

        add_time("11:43 AM", "00:20")
        # Returns: 12:03 PM

        add_time("10:10 PM", "3:30")
        # Returns: 1:40 AM (next day)

        add_time("11:43 PM", "24:20", "tueSday")
        # Returns: 12:03 AM, Thursday (2 days later)

        add_time("6:30 PM", "205:12")
        # Returns: 7:42 AM (9 days later)
'''
    tm = TimeManipulator("6:30 PM", "205:12")
