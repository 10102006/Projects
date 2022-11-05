"""
STATUS: Working

OVERVIEW: back-end

IMPROVEMENTS:
    - TODO Readthrough

What to do:
    1. Database:
      1. filename => date + id
      {
          "Id": {[id = enumerator]};
          "Name": {string};
          "Priority": {int};
          "Completed": {bool};
          "Description": {string};
      }

path: E:\Coding\Python Codes\Projects\TO-DO\Database
path-II: TO-DO\Database

"""

# @ Imports
import os
from os import path
import json
import shutil
# $ from datetime import date

# * Defining


class Database:
    def __init__(self, path):
        """
            - path for the database is stored in var {database_path}
            - Initiating ->ID() method for enumeration
        """
        self.database_path = path

        # - Changing the directory for easier file operations
        os.chdir(self.database_path)

        self.ID()

    def ID(self, function=0):
        """
            - this is the initialization for the id enumerator for the {TaskId} class
            - use of the param {function} is to check what is needed:
            - if 0 then initializing the file for the id enumeration storage
            - if 1 then the reading and setting of the starting enumeration is took place
        """
        # - Creating a file for the storage of the last id index
        if function == 0:
            if not path.isfile(path.join(self.database_path, "ID.txt")):
                with open("ID.txt", "w") as id_file:
                    id_file.write("1")

        # - Reading and Initialization of the first enumeration
        elif function == 1:
            with open("Id.txt", "r") as id_file:
                return int(id_file.readline())

    @staticmethod
    def SaveFile(data):
        """ - this is for creation of file for the task object in form of {data}"""
        # $ - making a special file name using the index and task id => Implement later
        # filename = f"{date.today()}-{data.get('Id')}"

        filename = f"Task-{data.get('Id')}"

        # - using json file dumping for the file creation
        with open(f"{filename}.json", "w") as json_file:
            json.dump(data, json_file)

    @staticmethod
    def LoadFile(taskId):
        """ - this is for retrieving of the task from the file created using the param {taskId}, which corresponds to the task id"""
        filename = f"Task-{taskId}"

        # - retrieving the data using the json load() in dict format
        with open(f"{filename}.json", "r") as json_file:
            data = json.load(json_file)
            return data

    def ChangeFile(self, taskId, completed=True):
        """ - implementation of the #checked function of the To-Do-List by change the value of the {completed} attribute of the task dict"""
        # - retrieving the data of the task in dict formate
        data = self.LoadFile(taskId)

        # - changing of the completed attribute
        data.__setitem__("Completed", completed)

        # - overwriting the task json file for change implementation
        self.SaveFile(data)

    def TrashFile(self, taskId):
        """ - moving the task of id => {taskId} from the database folder to the #Trash folder"""
        filename = f"Task-{taskId}.json"
        shutil.move(path.join(self.database_path, filename),
                    path.join(self.database_path, "Trash"))

    def CleanTrash(self, confirm=False):
        # $ Make a retrieve trash function as well as reduce the file size of the trash files ;)
        """ - removing the trash files from the trash folder in the database folder"""
        os.chdir(path.join(self.database_path, "Trash"))
        trashFiles = os.listdir()

        # - removing the files via os.remove()
        if confirm:
            for filename in trashFiles:
                os.remove(path.join(self.database_path, filename))

        # - rechanging the path for convenience
        os.chdir(self.database_path)


class TaskId(Database):
    def __iter__(self):
        """
            - initialisation of a {id} enumerator
            - using the {ID()} method of the {Database} class for getting the initial value of {id}
        """
        self.id = self.ID(1)
        return self

    def __next__(self):
        """
            - defining the funtionality of the enumerator.next()
            - making a temp var for the return value
            - incrementing the {id} enumerator and updating the storage file with the new value
        """
        current_id = self.id
        self.id += 1

        with open("Id.txt", "w") as id_file:
            id_file.write(str(self.id))

        return current_id

    @staticmethod
    def resetId():
        """ - for reseting the value of the id enumerator"""
        # - change the file value
        with open("Id.txt", "w") as id_file:
            id_file.write('1')


# ? Implementation
if __name__ == "__main__":
    pass
    # database = Database(database_path)

    # _id = TaskId(database_path)
    # Id = iter(_id)

    # task_test = Task("Studying", 1, "Revise for Maths test tomorrow")

    # database.SaveFile(task_test)

    # print(database.LoadFile(8))
    # database.ChangeFile(8, False)
    # print(database.LoadFile(8))

    # database.RemoveFile(8)
