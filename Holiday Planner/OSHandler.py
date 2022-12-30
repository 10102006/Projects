"""
STATUS: Working

OVERVIEW: For backup the datbase of Holiday Planner

IMPROVEMENTS:
    - TODO Add sq database
    - Add Decorators -> too many chdir
    - Add more Safe Checks

"""

# @ Imports
import os
from os import path, chdir
from os.path import join
import json

# * Defining


class Dumper:
    """
    Handler for making a folder tree of State object
    """

    def __init__(self, database):
        """
        Initialise rootdir and database
        """
        self.rootdir = r"E:\Coding\Projects\Holiday Planner\Database"
        chdir(self.rootdir)

        self.database = [state.GetState() for state in database]

    def Activate(self):
        """
        Command to make backup.
        """
        self.InitialiseStates()

    def InitialiseStates(self):
        """
        Making State fldrs and Detail files
        """
        for state in self.database:
            chdir(self.rootdir)
            statedir = join(self.rootdir, state["Name"])

            if not path.exists(statedir):
                os.mkdir(state['Name'])
                chdir(statedir)

                with open("Description", "x") as file:
                    file.write(state['Description'])
            else:
                os.chdir(statedir)

            self.InitialiseTouristPlace(state)

    def InitialiseTouristPlace(self, state):
        """
        Making a json file form tourist-place
        """
        for touristPlace in state['TouristPlaces']:
            os.chdir(join(self.rootdir, state['Name']))

            with open(touristPlace['Name'], "w") as file:
                json.dump(touristPlace, file, indent=2)
