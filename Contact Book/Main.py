"""
STATUS: Barely
OVERVIEW:
IMPROVEMENTS:
Workings:

- Sorted List Contacts

"""

# @ Imports

import os
from cmd import Cmd

from Contact import Contact
from DatabaseHandler import Handler

# * Defining


class Program():
    def __init__(self):
        """
        Initialising handler.
        """
        self.handler = Handler()

    def do_quit(self, args):
        """
        Quits the program.
        """
        print("Quitting...")
        raise SystemExit

    def do_save(self, args=[]):
        """
        """
        name = input("Enter Name: ")
        number = int(input('Enter Number: '))

        try:
            contact = Contact(name, number)
            self.handler.AddContact(contact)
        except:
            print(Exception)

    def do_update(self, args=[]):
        """
        """
        name = input("Enter Name: ")
        info = int(input('What to update(1-Alias, 2-PhoneNumber, 3-Email): '))
        value = input("Next/New value: ")

        match info:
            case 1:
                info = 'Alias'
            case 2:
                info = 'PhoneNumbers'
            case 3:
                info = 'Email'

        self.handler.Database[name].Update(
            info, int(value) if value.isnumeric() else value)
        self.handler.Sync()

    def do_delete(self, args=[]):
        """ """
        name = input("Enter Name: ")
        del self.handler.Database[name]
        self.handler.Sync()
        os.remove(os.path.join(self.handler.rootdir, name))

    def do_list(self, args=[]):
        """ """
        for contact, info in self.handler.Database.items():
            print(contact, info.PhoneNumbers[0])


# ? Implementation
if __name__ == "__main__":
    prompt = Program()
    prompt.do_save()
    prompt.do_delete()
    prompt.do_update()
    prompt.do_list()
