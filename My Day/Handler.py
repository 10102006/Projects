'''
STATUS: Working

OVERVIEW: Handles the back-end of the program

IMPROVEMENTS:
    -TODO Read through First

'''


# @ Imports
from ntpath import join
import os
from os import path, remove

import json

from datetime import datetime, time

database_path = join(os.getcwd(), r'My Day\Database')

# * Defining


class Database:
    def __init__(self, path):
        """ So this functions makes a class a constructor. """
        self.databasePath = join(path)
        os.chdir(path)

    def CreateSlot(self, name=str, startingTime=(), endingTime=()):
        """
            - Using a certain mechanic for finding time
            - And filling in the values given as param in a dict
            - Finding the index using the ```Database.SetIndex()``` method
            - Returning the dict object formed
        """
        # - In a concatenated way finding if the time values are in a tuple or time format and taking according actions
        # - If the param is tuple then making a time obj using the tuple values
        # - Else using the time obj as it is

        startingTime, endingTime = (
            item if type(item) == datetime.time
            else time(
                int(item[0]),
                int(item[1])
            ) for item in [startingTime, endingTime]
        )

        slot = {
            "Index": 0,
            "StartingTime": startingTime,
            "EndingTime": endingTime,
            "Name": name,
        }

        Database.SetIndex(slot)
        return slot

    @staticmethod
    def SaveSlot(slotObject):
        """Saving a json file with the index of the slot and storing the data in it"""
        filename = f"{slotObject['Index']}.json"

        if not path.isfile(filename):
            with open(filename, "w") as file_obj:
                # - Using json dump to save the slotObject data
                json.dump(slotObject, file_obj, indent=4, default=str)

    @staticmethod
    def LoadSlot(filename):
        """Retrieving the data store in a specific file"""
        filename = filename if ".json" in filename else f"{filename}.json"

        with open(filename, "r") as file_obj:
            # - Using json load for retrieving the data
            slot = json.load(file_obj)

            # - Converting string time -> datetime time
            slot.update({
                timePeriod: datetime.strptime(
                    slot[timePeriod], "%H:%M:%S").time()
                for timePeriod in ["StartingTime", "EndingTime"]
            })

            return slot

    @staticmethod
    def SetIndex(slotObject):
        """
            - Looping through all the files/slots in the database dir
                - Checking if the ```StartingTime``` of the ```slotObject``` is greater than the current iterating file/slot
                - if yes then return the index of the iteration

            - Else if the for loop return empty then returning the number of files present in the database, meaning the last index
        """

        # - Looping using enumerate for index counting
        for index, file in enumerate(sorted(os.listdir(), key=len), start=1):
            slot = Database.LoadSlot(file)

            startingTime = slot.get("StartingTime")

            # Checking mechanism
            if slotObject["StartingTime"] < startingTime:
                slotObject["Index"] = index
                return
        else:
            # - returning the last index
            slotObject["Index"] = (len(os.listdir()) + 1)

    def AdjustSlot(self, slotObject):
        """
            - Storing all the data of the slots in a list
            - Add the new ```slotObject``` in the list at a certain index
            - Remaking the files in the correct order
        """
        slots = []
        index = slotObject["Index"]

        # - Loading and Appending the slot data into the slots list
        # - removing the files for further ease
        for slot in os.listdir():
            slots.append(self.LoadSlot(slot))
            remove(slot)

        slots.insert(index - 1, slotObject)

        # - Remaking the files in the correct order
        for slotIndex, slot in enumerate(slots, start=1):
            slot["Index"] = slotIndex
            self.SaveSlot(slot)


# ? Implementation
if __name__ == "__main__":
    database = Database(database_path)

    # # Single unique slot
    # slot = database.CreateSlot(
    #     "test",
    #     startingTime=(int(input(". ")), 0),
    #     endingTime=(int(input(".. ")), 0)
    # )

    # print(slot)

    # Saving the unique slot
    # database.SaveSlot(slot)

    # # Retrieving the Saved slot
    # os.chdir(r'E:\Coding\Projects\My Day\Database')
    # slot = database.LoadSlot('9')
    # print(slot)

    # Placeholder slots
    print(os.getcwd())
    for index in range(5):
        slot = database.CreateSlot(f"Task-{index}", (10 + index * 2, 0), (10 + index * 2, 0))
        print(slot)
        database.SaveSlot(slot)


    # Rearranging the slots to accommodate the new slot
    # database.AdjustSlot(slot)
