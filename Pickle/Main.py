"""
STATUS: Working

OVERVIEW: File performing basic python keytype class storage

IMPROVEMENTS:
    - Find more usability of the module

What to do:
    1. Save the text from the link => request
    2. Obtain all the lines in a list
    3. Pickle the list in new file => pickle
    4. Make pickle file a reading function

"""

# @ Imports
import os
import pickle

# * Defining

os.chdir('E:\Coding\Projects\Pickle')

list_data = []

def StorePickleFile(data, filename):
    """
    What is done:
        1. filename confirmation this will add the '.pkl' format if the format is not avail
        2. Then we will make a file with the filename with binary encoding
        3. When the file is made then we will add the data to the file
    """
    filename = filename if '.pkl' in filename else f'{filename}.pkl'
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

def RetrievePickleFile(filename):
    """
    What is done:
        1. Filename confirmation this will add the '.pkl' format if the format is not in the given filename
        2. Then we will open the file with the given filename in read mode
        3. Then using the pickle module we will retrieve the data
        4. We will store this data and return it
    """
    filename = filename if '.pkl' in filename else f'{filename}.pkl'
    with open(filename, 'rb') as file:
        data = pickle.load(file)
        return data

# ? Implementation
if __name__ == "__main__":
    data = RetrievePickleFile('data')
    for item in data:
        print(item)

