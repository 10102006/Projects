'''
STATUS: Not Optimised

OVERVIEW: Directory formatter with certain functionings

IMPROVEMENTS:

Workings:
      *1. MakeRandomFiles(numberOfFile) => This method will make random file with random capitalisation of first letter
      *2. GetFiles(folderpath) => This function will get all the files get there format and store them in different lists
      *3. RenamingOffiles() =>
           1. CapitaliseFiles(filecapitalised) => This method will get the files and then capitalise them
           2. NumberFormat() => This Method will numberise the files of a specific format
           3. LeaveFile(fileNumbered) => This function will remove the file from the list whose file of the files
       4. Format() => This function will unite the methods to do the job

'''

# * Imports
import os
from os import path

# @ Defining


class FolderPrettier:
    """
      This class will contain all the different function required
      for the formatting and in the main function it will do it all
    """
    # ? These are the format that will be generated with MakeRandomFiles() list

    def __init__(self, t_path):
        '''
          This is the constructor of your class
          This will initialise the path of the folder
        '''
        self.folderpath = path.join(t_path)
        os.chdir(self.folderpath)

    def MakeRandomFiles(self, numberoffiles):
        """
          This function will name a file with random name
          and random format from list of format names

          Then this will initialise the file this will run once
        """
        import string
        import random

      # ? This is the list for the file names
        filenames = []

      # @ This will randomly name the files
        for _ in range(numberoffiles):
            pass
        # ? Use this in choice for including the numbers (string.ascii_letters + string.digits)
            r_filename = ''.join(random.SystemRandom().choice(
                string.ascii_letters) for _ in range(6))

        # * This will add the format to the file
            r_format = ".txt"
            # r_format = random.choice(self.formats)

            c_filename = f'{r_filename}.{str(r_format)}'
            filenames.append(c_filename)

      # @ This will make the files in the folder Formatter
           # ! This is the in which I will log all the file names
            with open('r_filename.txt', 'w') as filedir:
               # * This is changing the dir to the folder
                os.chdir(self.folderpath)

               # @ This will loop through all the file names generated
                for file in filenames:
                  # * This will log the file names in the r_filename.txt
                    filedir.write(f'{file} \n')
                   # ! This code will create the files
                    with open(file, 'w') as _file:
                        _file.write('Lorem Ipsum Dorem')

    @staticmethod
    def GetFiles(folderPath, formatoflist=0):
        """
            params:
                1. folderpath => For the specifing the folder
                2. formatoflist => For the specific type of list eg: py, txt

            This method will get all the files in the path of the folder and
            then segregate them in respective format
        """
        m_files = os.listdir(folderPath)
        numerisedfiles = []

        if formatoflist:
            for _file in m_files:
                if formatoflist in _file:
                    numerisedfiles.append(_file)
            return numerisedfiles

        elif formatoflist == 0:
            return m_files

    def RenamingOfFiles(self, c_file, fileNumbered=[]):
        """
         Things done:
            1. Changing the dir so we can get the directory
            2. Looping through file given to us as c_file
            3. If the numerised file list is given then we will iterate with enumerate to get the index
            4. Then we will rename the specific file

        """

        os.chdir(self.folderpath)

        for c_file in c_file:
            os.rename(c_file, c_file.capitalize())

        for index, file_name in enumerate(fileNumbered):
            if "_" in file_name:
                file_name = file_name[2:]

            new_filename = f'{index+1}_{file_name}'
            os.rename(file_name, new_filename)
            print(new_filename)

    def Format(self, formatToBeNumerized=''):
        """
            Done:
                  1. Intialising main format list
                  2. Capitalising the list
                  3. Then we will try to make the Files numerised
                  4. At first we will check if the path is none or not
        """

      # * Capitalisation files
        m_files = self.GetFiles(self.folderpath)

      # * Numerication of files
        try:
            n_files = self.GetFiles(self.folderpath, formatToBeNumerized)
            self.RenamingOfFiles(m_files, n_files)

        except:
            print('You have not put any format so nothing will be numerised')


# ? Execution

if __name__ == "__main__":
    formatter = FolderPrettier(
        "E:\Coding\Projects\Folder Formatter\Database")
    # Formatter.Format('txt')

    formatter.Format('txt')
