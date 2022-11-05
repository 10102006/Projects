"""
STATUS: Working

OVERVIEW: Uses `Cryptographer` to make encrypted password files and loading/decrypting the said made file.

IMPROVEMENTS:
    - Implement SQLite
"""

# @ Imports

import os
from os.path import join
import stdiomask

from Cryptographer import Cryptographer as cp

database_path = join(os.getcwd(), r'Password Manager\Database')

# * Defining


class Manager():
    """ Main class responsible for password saving. """

    def __init__(self, path):
        """ So this functions makes a class a constructor """
        self.databasePath = path
        os.chdir(path)

        self.MasterPassword()

    @staticmethod
    def MasterPassword(masterPassword=""):
        """ Generates Master Password File.
            - Checking is Master_Password file is made.
            - Taking according actions.
            - Using stdiomask to make hidden input box.Sa
        """
        if not os.path.isfile('Master_Password.key'):

            # - Checking if masterPassword is given or not, using stdiomask for input type.
            masterPassword = masterPassword if masterPassword else stdiomask.getpass(
                "Enter Master Password: ")

            Manager.SavePassword('master_password.key', masterPassword)

    @staticmethod
    def SavePassword(filename, password):
        """ Saving a given password in encrypted format. """
        filename = f"{filename}.key" if ".key" not in filename else filename

        # - Starting a try-excepting block.
        try:
            encrypted_password = cp.EncryptPassword(password)

            # - Generating password file.
            if not (os.path.isfile(filename)):
                with open(filename, 'wb') as password_file:
                    password_file.write(encrypted_password)

            # - Overriding previous password
            else:
                print(
                    'This password-filename is already taken do you want to override it.')
                print('Previous password: ', Manager.LoadPassword(filename))

                if (True if input('Enter 1 to confirm: ') == '1' else False):
                    with open(filename, 'wb') as password_file:
                        password_file.write(encrypted_password)

        except Exception as exception:
            print(exception)
            print('Your password is not saved!')

        else:
            print('Password saved successfully!')

    @staticmethod
    def LoadPassword(filename):
        """ This function will be used to retrieve the passwords. """
        filename = filename if '.key' in filename else f"{filename}.key"

        try:
            en_password = open(filename, 'rb').read()
            decryptedPassword = cp.DecryptPassword(en_password)

        except Exception as exception:
            print(exception)

        else:
            return decryptedPassword


# ? Implementation
if __name__ == "__main__":
    mn = Manager(database_path)

    # - Taking inputs
    filename = input('Filename: ')
    password = input('Password: ')

    # - Saving file with encrypted password
    print('-----------------------------------------')
    mn.SavePassword(filename, password)

    # - Checking if the password can be decrypted
    print('-----------------------------------------')
    l_password = mn.LoadPassword(filename)
    print(f"{l_password} has been saved!")
