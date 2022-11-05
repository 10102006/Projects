"""
STATUS: Working

OVERVIEW: front-end

IMPROVEMENTS:
    - TODO Readthrough

Table = {
? Var of the class
    title = []
    rows = int

? Task values
    values = {
        ! All the attributes are list of the following
        "Id": {[id = enumerator]};
        "Name": {string};
        "Priority": {int};
        "Completed": {bool};
        "Description": {string};
}

}

"""

# @ Imports

# * Defining
task = {
    "Id": 5,
    "Name": "Groceries",
    "Priority": 2,
    "Completed": False,
    "Description": "Buy potato and ketchup"
}

titles = ["Id", "Name", "Priority", "Completed"]


class Table:
    def __init__(self, titles=[], rows=0):
        """
            - initialising var for storing information about the table
            - making a basic structure of the table using the param {titles}
            - returning the values of the table
        """
        self.titles = titles
        self.rows = rows

        self.values = {}

        if titles:
            self.SetTitles(titles)

        self.GetValues()

    def GetValues(self):
        """ - for getting the {values}"""
        return self.values

    def SetTitles(self, titles):
        """
        """
        self.titles = titles

        # - using the for loop for making an attribute in {values} dict with empty list for each title
        for title in self.titles:
            if not self.values.__contains__(title):
                self.values[title] = []

    def AddToTable(self, data):
        """
            - this will add data of the tasks => {data} to the table

            - For loop
                - repeating for all the attributes of the tasks => {titles}
                - adding the value of the attribute in the {data} to the correct attribute list in the table
                - if the attribute specified is not in the table then making an attribute

            - incrementing the {rows} var for convenience
        """
        for item in data.keys():

            # - Finding if the item is in the {titles} list
            if item in self.titles:
                value = data.get(item)

                # - adding the value of the item to the list of attributes
                self.GetValues().get(item).append(value)

            else:
                self.titles.append(item)

                # - making a seperate title for the item using dict
                self.values[item] = [data.get(item)]

        self.rows += 1


class Display():
    def __init__(self, table):
        """
            - making a variable for the table
        """
        self.table = table

    def PrintTable(self):
        """
        $ make this more optimal and beautiful to look, make it responsive if possible ;)

            - printing the titles with beautification
            - loop for printing the item along with the corresponding titles
        """
        print('-' * 48)
        [print(title, end=' | ') for title in self.table.titles]

        print()
        print('-' * 48)

        # - Running main loop for number of rows as there are that number of values inputted
        for index in range(self.table.rows):

            # - getting the values of the attributes along with the index to to find the values index in the attribute list
            for _, item in enumerate(self.table.values):
                # - printing the value from the attribute list
                if item == "Completed":
                    print(str(self.table.values.get(item)
                          [(index)]).ljust(5), end=' | ')
                elif item == "Id":
                    print('', self.table.values.get(item)[(index)], end=' | ')
                elif item == "Description":
                    print(self.table.values.get(item)[(index)], end='')
                else:
                    print(self.table.values.get(item)[(index)], end=' | ')
            print()

        print('-' * 48)


# ? Implementation
if __name__ == "__main__":
    pass
    toDoTable = Table(titles)
    display = Display(toDoTable)

    # print(toDoTable.values)

    for index in range(4):
        task["Id"] = index
        task["Priority"] = 4 - index
        task["Completed"] = True if index % 2 == 0 else False
        toDoTable.AddToTable(task)

    print(toDoTable.values)

    display.PrintTable()
