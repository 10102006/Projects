"""
STATUS: Not working

OVERVIEW: Uses [Handler] and [Viewer], to make a schedule and perform other functions

IMPROVEMENTS:
    - TODO check <do_align>

"""

# @ Imports
import os
from os import path, remove
from cmd import Cmd

from Handler import Database
from Viewer import Schedule

database_path = path.join(os.getcwd(), r'My Day\Database')

# * Defining


class MyDay(Cmd):
    def __init__(self):
        """So this functions makes a class a constructor"""
        self.database = Database(database_path)
        self.scheduleManager = Schedule(database_path, self.GetSlots())

        #  Making a schedule
        self.schedule = self.scheduleManager.MakeSchedule()

    def GetSlots(self):
        print(os.getcwd())
        slots = [self.database.LoadSlot(slot)
                 for slot in sorted(os.listdir(), key=len)]
        return slots

    def do_view(self, args):
        """This command will print the schedule."""
        # Printing the Schedule
        self.scheduleManager.PrintSchedule(self.schedule)

    def do_add(self, args):
        """This command will add a slot to the schedule using the input giving by user."""

        name = input("Enter slot name: ")
        startingTime, endingTime = (input(f"Enter slot {item}: ").split(
            '-') for item in ["starting time", "ending time"])

        slot = self.database.CreateSlot(name, startingTime, endingTime)
        print(slot)
        self.database.AdjustSlot(slot)

    def do_align(self, args):
        """This command will align any misaligned slots in the schedule."""
        slots = self.GetSlots()

        def StartingTime(slot):
            return slot.get('StartingTime')

        slots = sorted(slots, key=StartingTime)

        for index, slot in enumerate(slots, start=1):
            slot.update({'Index': index})
            print(slot)

        [remove(slot) for slot in os.listdir()]
        [self.database.SaveSlot(slot) for slot in slots]

    def do_quit(self, args):
        """Quits the program."""
        print("Quitting.")
        raise SystemExit


if __name__ == '__main__':
    prompt = MyDay()
    prompt.prompt = '> '
    prompt.cmdloop('Starting prompt...')
