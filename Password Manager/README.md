TODO Complete This

## Basic Overview

## Password Manager Look

COMMANDS:
    - Initialize > used for starting the program, checking if the `main_encryption_key` and `master_password` are present.
    - Save > saving a new password.
    - Delete > deleting a saved password.
    - Update > overriding saved password.

---
## Code Functionality

1. **Cryptographer**: This file will take care of encrypting and decrypting process of password managing.

    - Cryptographer: is the main class handling the process
        - GenerateKey( ): is used for generating the cryptic ```key``` used throughout the process.
        - LoadKey( ): is used for loading the ```key```.
        - EncryptPassword(givenPassword): encrypting the `givenPassword` using `Fernet`, return the `encryptedPassword`.
        - DecryptPassword(encryptedPassword): decrypting the `encryptedPassword`, return `decryptedPassword`

``` python
if __name__ == "__main__":
    cp = Cryptographer(database_path)

    # - Generating the key
    cp.GenerateMainKey()

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
```

---

2. **Handler**: This file will take care of os handling process.
   - Manager: is the main class handling all the process.
     - MasterPassword(masterPassword): checks where the `master_password.key` is made or not, if not then making one.
     - SavePassword(filename, password): save a password file with the `filename` and encrypted `password` as content.
     - LoadPassword(filename): reading the contents of `filename` and decrypting the contents, returning `decryptedPassword` if no error.

``` python
if __name__ == "__main__":
    mn = Manager(database_path)

    # - Taking inputs
    filename = input('Filename: ')
    password = input('Password: ')

    # - Saving file with encrypted password
    mn.SavePassword(filename, password)

    # - Checking if the password can be decrypted
    l_password = mn.LoadPassword(filename)
    print(f"{l_password} has been saved!")
```

3. **Main**: CLI application working in front.
