"""
STATUS: Not Working

OVERVIEW: Should work as a notes manager with [pickle]

IMPROVEMENTS:
    -TODO Readthrough First

Notes template:
    => {
        name: ''
        description:''
        notes:['','']
    }

"""

# @ Imports
import pickle
import os
from os import path
from os.path import join

# * Defining
class Main:
    """ """

    def __init__(self, database_directory):
        """
        So this functions makes a class a constructor
        """
        self.database_directory = database_directory

    def MakeList(self, list_name, list_description, notes=[], publish=False):
        """
        Making a note_object and return it
        """
        list_object = {
            "name": list_name,
            "description": list_description,
            "notes": notes,
        }
        if publish:
            self.PublishList(list_object)

        return list_object

    def EditList(self, list_object, editing_detail, what_to_edit=3, republish=False):
        """
        This function will be used to edit the list_object
        If the what_to_edit is:
            1. => name of list
            2. => description of list
            3. => (default) List of notes
        """
        previous_name = list_object.get("name")

        list_object.update(
            {
                "name"
                if what_to_edit == 1
                else "description"
                if what_to_edit == 2
                else "notes": editing_detail
            }
        )

        if republish:
            os.remove(f"{previous_name}.pkl")
            self.PublishList(list_object)

    def PublishList(self, list_object, file_path=""):
        """
        This function will make a pkl file of the list_object in the database folder
        """
        os.chdir(self.database_directory if not file_path else file_path)
        filename = list_object.get("name")

        filename = filename if ".pkl" in filename else f"{filename}.pkl"

        try:
            with open(filename, "wb") as file:
                pickle.dump(list_object, file)
            print(f"{filename} > sucessfully made")

        except Exception as exception:
            print(exception)
            print(filename)

    def RetrieveList(self, list_name):
        """
        This function will retrive the pkl file we made with the previous function and return the => list_object
        """
        os.chdir(self.database_directory)

        list_name = list_name if ".pkl" in list_name else f"{list_name}.pkl"

        with open(list_name, "rb") as file:
            list_object = pickle.load(file)
            return list_object


class Console(Main):
    """
    This class will help us to use the previous class with console
    """

    @staticmethod
    def ChooseItemFromList(given_list):
        """ """
        for index, item in enumerate(given_list, 1):
            print(f"{index}. {item}")
        item_index = input("Enter index of the item: ")

        if item_index.isnumeric():
            item = given_list[int(item_index) - 1]

            return item

    def MakeList(self):
        """ """

        def GenerateList(temporary_list=[]):
            """
            This function will take input until an empty string is given and store all the string in a list => return this list
            """
            while True:
                item = input("> ")
                if item:
                    temporary_list.append(item)
                else:
                    break

            return temporary_list

        name = input("Enter name of list: ")
        description = input("Enter list description: ")
        notes = GenerateList()

        list_obj = Main.MakeList(self, name, description, notes, True)

        return list_obj

    def EditList(self, database_path):
        """ """
        os.chdir(database_path)
        lists = os.listdir(database_path)

        list_name = self.ChooseItemFromList(lists)

        print(list_name)

        list_obj = Main.RetrieveList(list_name[:-4])

        what_to_edit = input(
            "What do you what to edit(1:name, 2:description, 3:notes): "
        )
        print("------------------------------------------")
        if what_to_edit == "3":
            edit_obj = self.GenerateList()
        else:
            edit_obj = input(
                f'Enter {"name" if what_to_edit == "1" else "description"} of the list: '
            )

        Main.EditList(list_obj, edit_obj, what_to_edit, True)


# ? Implementation
if __name__ == "__main__":
    databasePath = f"{os.getcwd()}\\Notes App\\Database"
    print(databasePath)

    main = Main(databasePath)
    cmd = Console(databasePath)

    t_list = cmd.MakeList()
    print(t_list)

    # cmd.EditList(Mpath)

    # t_list = MakeList('Test', 'test-I')

    # print(t_list)
    # EditList(t_list, ['test_obj_I', 'test_obj_II'], 3)

    # print(t_list)

    # PublishList(t_list, Mpath)
    # t_list = RetrieveList('Test', Mpath)
    # print(t_list)

    # EditList(t_list, 'Test_name_II', 1, True)

    # t_list = RetrieveList('Test_name_II', Mpath)
    # print(t_list)
