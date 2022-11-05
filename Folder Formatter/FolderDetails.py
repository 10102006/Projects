'''
STATUS: Should Be Remade

OVERVIEW: This file will make a folder tree that will be storeded in a list

IMPROVEMENTS:
    -

Tasks:

'''

# * Imports
import os
from os import chdir, getcwd, listdir, path

# @ Defining


def FolderDetails(folder_path, details_required=1, files=[], folders=[], main_function=True):
    """
    This a recursive method so this will repeat itself

    Things done:
        1. First looping though all the dir in the path
        2. Making a path with the dir name
        3. If the dir is a folder then we will recurse again but with the path that we defined earlier
        4. If the dir is a file then we will print the dir with extension of choice
        5. For cleaing we are index the level of folder heritage
    """
    folder_listDir = os.listdir(folder_path)

    for dir in folder_listDir:
        dir_path = path.join(folder_path, dir)

        if path.isfile(dir_path):
            files.append(dir)

        else:
            if main_function:
                folders.append(dir)
                os.chdir(dir_path)

                FolderDetails(dir_path, details_required,
                              files, folders, False)

    if details_required == 1:
        return files
    elif details_required == 2:
        return folders
    else:
        return(files, folders)


if __name__ == "__main__":
    t = FolderDetails("E:\Coding\Projects", 0)
    print(t)
    # # [print(i) for i in t]