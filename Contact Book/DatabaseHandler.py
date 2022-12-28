"""
STATUS: Working

OVERVIEW: Basic Database Handling with json

IMPROVEMENTS:
    - Add SQlite
    - Use Pathlib
"""

# @ Imports

import os
import json

from Contact import Contact

# * Defining


class Handler:
    def __init__(self):
        """
        - Iniitalising Database
        - Syncing database
        """
        self.rootdir = r'E:\\Coding\\Projects\\Contact Book\\Database'
        os.chdir(self.rootdir)
        self.Database = {}

        self.SetDatabase()
        self.Sync()

    def AddContact(self, contact=Contact):
        name = contact.get()['Alias'][0]
        self.Database[name] = contact
        self.Sync()

    def SetDatabase(self):
        """
        For add the previous contacts to the database
        """

        def setContact(contact):
            """
            FIXME Shitty code Remove this
            """
            alias = contact['Alias']
            numbers = contact['PhoneNumbers']
            email = contact['Email']

            set = Contact(alias[0], numbers[0])
            set.Update('Alias', alias)
            set.Update('PhoneNumbers', numbers)
            set.Update('Email', email)

            return set

        for contact in os.listdir(self.rootdir):
            with open(contact, "r") as file:
                info = json.loads((file.read()))
                self.Database[contact] = setContact(info)

    def Sync(self):
        """
        Making json files for each database entry
        """
        os.chdir(self.rootdir)
        for contact in self.Database:
            with open(f"{contact}", "w+") as file:
                json.dump(self.Database[contact].__dict__, file, indent=3)
