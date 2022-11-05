'''
Status: Working

Overview: Does the front-end work of the program

Improvement:
    -TODO Read through First

'''


# @ Imports

from datetime import time

import os
from os import path
from ntpath import join


database_path = join(os.getcwd(), r'My Day\Database')

# * Defining
Slots = [
    {
        "Index": 1,
        "Name": "Break",
        "StartingTime": time(10, 00, 00),
        "EndingTime": time(11, 00, 00),
    },
    {
        "Index": 2,
        "Name": "Skills",
        "StartingTime": time(13, 00, 00),
        "EndingTime": time(13, 30, 00),
    },
    {
        "Index": 3,
        "Name": "Novel",
        "StartingTime": time(20, 00, 00),
        "EndingTime": time(22, 00, 00),
    },
    {
        "Name": "Jogging",
        "StartingTime": time(12, 45, 00),
        "EndingTime": time(13, 45, 00),
        "Index": 5
    }
]


class Schedule:
    def __init__(self, path, slots):
        """
            So this functions makes a class a constructor
        """
        self.databasePath = path
        self.slots = slots
        self.schedule = {f"{title}": [] for title in ['Name', 'Index', 'StartingTime', 'EndingTime']}

    def MakeSchedule(self):
        """
            - Looping through all the given ```slots```
                - Looping through all the keys in the slot dict
                - Add all the items of the slot to the ```schedule``` obj.

            - Return the ```schedule``` obj
        """
        for slot in self.slots:
            for item in slot:
                self.schedule[item].append(slot[item])

        return self.schedule

    def PrintSchedule(self, schedule=''):
        """
            - Making a temp ```schedule``` var
            - Printing the titles using a short-hand loop
            - Printing the values of the schedule with justification
        """
        schedule = schedule if schedule else self.schedule

        # - All the keys of the schedule obj
        [print(key, end=" | ") if key != "Name" else None for key in schedule]
        print("Name...")

        print('-' * 43)

        # - Using for loop to get all the index in the schedule
        for index, item in enumerate(sorted(schedule["Index"])):

            # - Printing the index
            print(str(item).rjust(4), end=". | ")

            # - Getting the StartingTime and the EndingTime using a short-hand loop
            startingTime, endingTime = ((schedule[timePeriod][index]).strftime(
                "%H:%M:%S") for timePeriod in ["StartingTime", "EndingTime"])

            # - Printing the StartingTime
            print(startingTime.center(12), end=' - ')

            # - Printing the EndingTime
            print(endingTime.center(10), end=' | ')

            # - Printing the name of the task
            print(schedule["Name"][index])


# ? Implementation
if __name__ == "__main__":
    scheduleManager = Schedule(database_path, Slots)

    #  Making a schedule
    schedule = scheduleManager.MakeSchedule()

    # Printing the Schedule
    scheduleManager.PrintSchedule(schedule)
