"""
STATUS: Working

OVERVIEW: Takes care of encrypting and decrypting process

IMPROVEMENTS:
    - Understand it's deeper concept

"""

# @ Imports
import stat
from cryptography.fernet import Fernet

import os
from os.path import join

database_path = join(os.getcwd(), r'Password Manager\Database')

# * Defining


class Cryptographer():
    """ Class responsible for password encrypting and decrypting. """

    def __init__(self, path):
        """ So this functions makes a class a constructor. """
        self.databasePath = path
        os.chdir(path)

    def GenerateKey(self):
        """ This is one time function which we will run in the starting to make a key which will be used to encrypt and decrypt the passwords.
            - Generating an soft key and storing it in a file
            - This ```key``` is most important aspect of in cryptography process
        """
        os.chdir(self.databasePath)
        key = Fernet.generate_key()

        with open("main_encryption_key.key", "wb") as key_file:
            key_file.write(key)

    @staticmethod
    def LoadKey():
        """ Loading the ```key```"""
        print(os.getcwd())
        # - Here we are opening the special file, 'rb' is a special mode for key extension
        return open("main_encryption_key.key", "rb").read()

    @staticmethod
    def EncryptPassword(givenPassword):
        """ The function responsible for encrypting.
            - Using the ```LoadKey()``` to get the cryptic key
            - The using the Fernet module for encrypting the message
            - Returning the encrypted message
        """
        key = Cryptographer.LoadKey()

        # - Encoding the message in a certain format with the Fernet module to encrypt it
        encodedPassword = givenPassword.encode()

        # - Encrypting the message/password
        fernetKey = Fernet(key)
        encryptedPassword = fernetKey.encrypt(encodedPassword)

        return encryptedPassword

    @staticmethod
    def DecryptPassword(encryptedPassword):
        """ The function responsible for decrypting.
            - Loading the key using `LoadKey()`
            - Using the `Fernet` to decrypt the message
            - Returning the decrypted password
        """
        key = Cryptographer.LoadKey()

        # - Decrypting the password
        fernetKey = Fernet(key)
        decryptedPassword = fernetKey.decrypt(encryptedPassword).decode()

        return decryptedPassword


# ? Implementation
if __name__ == "__main__":
    cp = Cryptographer(database_path)

    # - Generating the key
    cp.GenerateKey()

    #  - Loading the key
    key = cp.LoadKey()

    # - Encrypting a password
    password = 'HelloWorld~!'
    en_password = cp.EncryptPassword(password)
    print(en_password)

    # - Decrypting the encrypted password
    dc_password = cp.DecryptPassword(en_password)

    if password == dc_password:
        print(':)')
