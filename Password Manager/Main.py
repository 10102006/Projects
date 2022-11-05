'''
STATUS: Working

OVERVIEW: Workable Password manager with encrypting and decryption

IMPROVEMENTS:
    - Should hide the encryption key and main password file
    - Multiple user and backup secured.
    - Delete all the password if the master password is not avail

'''


# * Imports

from ntpath import join
import os
from os import path
from cmd import Cmd


from Cryptographer import Cryptographer as cp
from Handler import Manager as mn

database_path = join(os.getcwd(), r'Password Manager\Database')
os.chdir(database_path)

# @ Defining

class Main(Cmd):
    def __init__(self):
        """ So this functions makes a class a constructor. """
        self

    def do_help(self, arg: str) -> bool | None:
        return super().do_help(arg)

# ? Execution

if __name__ == "__main__":
    main = Main()
    main.prompt = '> '
    main.intro = "Password Manager version: 1.1"

    main.cmdloop()

