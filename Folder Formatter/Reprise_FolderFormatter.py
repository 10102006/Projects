"""
STATUS: Not Working

OVERVIEW: Functions like the previous program with some light coding only not many features

IMPROVEMENTS:

Workings:
    1. Capitalise file names
    2. Make a folder for each format => Special name for folder*
    *** 3. Detailed file for the formatter history
            1. Date formatted
            2. Total number of files

"""

# * Imports
import os
from os import path
from FolderDetails import FolderDetails

_path = path.join('E:\Coding\Projects\Folder Formatter\Database')
os.chdir(_path)

# @ Defination

def FormatFilenames(folderpath=_path, shouldNumerised=False):
    """
    What to do:
        1. Obtaining all the names of the files in the folder
        2. Looping through the files and capitalising the names
        3. If the files should be numerised then lopping through the files then the files will be numbered
    """
    # * Obtaining the filenames with the FolderTree file
        # ? The detail_required is 1 by default
    files = FolderDetails(folderpath)

    os.chdir(folderpath)

    for file in files:
        os.rename(file.capitalize())
        print(file)

    print('----------------------------------------------------------------------')

    if shouldNumerised:
        for index, file in enumerate(files, 1):
            n_filename = f'{index}_{file}'
            os.rename(n_filename)


def ExtractFormats(folderpath=_path):
    """
    """
    folderpath = path.join(folderpath)
    files = FolderDetails(folderpath)

    formats = []

    for file in files:
        _, format = file.rsplit('.')
        if format not in formats:
            formats.append(format)

    return formats


# ? Implementation
if __name__ == "__main__":
    FormatFilenames(shouldNumerised=True)
