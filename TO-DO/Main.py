'''
STATUS: Working

OVERVIEW: CLI aplication for handling todos I think

IMPROVEMENTS:
    - TODO Readthrough

'''


# @ Imports
import typer
import os
from Database import Database, TaskId
from Viewer import Table, Display

database_path = "E:\Coding\Projects\TO-DO\Database"

# @ Initialising the basic ammenities

# $ remove it some how
titles = ["Id", "Name", "Priority", "Completed", "Description"]

# - typer init
app = typer.Typer()

# - database init
database = Database(database_path)

Id = TaskId(database_path)
id = iter(Id)

# - viewer init
toDoTable = Table(titles)
display = Display(toDoTable)

# * Defining

Tasks = []


def Task(name, id, priority=5, description=None):
    description = description if description else name
    """
    a simple method for making a task object in dict format using params and returning it for storage
    """
    task = {
        "Id": id,
        "Name": name,
        "Priority": priority,
        "Completed": False,
        "Description": description
    }

    return task


@app.command()
def add(taskname: str, priority: int = 0, description: str = ''):
    """
    used for adding tasks in the to-do-list
    """
    try:
        # - making a task object using {Task()} and storing it the database
        task = Task(taskname, next(id), priority, description)
        database.SaveFile(task)
    except:
        print('error')
    finally:
        view()


@app.command()
def view():
    """
    this is for viewing the task at hand in table formate
    """
    # - finding all the task files in the database
    for task in os.listdir(database.database_path):
        # - finding the id of the task at hand
        if "Task-" in task:
            taskId = int(task.split('-')[1].split('.')[0])

            # - retrieving the stored task using the id
            task = database.LoadFile(taskId)

            # - adding the task retrieved in the {Tasks}
            Tasks.append(task)

    # - adding the tasking at hand in the table and printing the table
    for task in Tasks:
        toDoTable.AddToTable(task)

    display.PrintTable()


@app.command()
def completed(taskid: int):
    """
    for marking the completed tasks as completed
    """
    database.ChangeFile(taskid)


@app.command()
def remove(taskid: int):
    """
    to remove a certain task using id of the task
    """
    # - checking if the task is completed or not if it then only trashing the task
    if database.LoadFile(taskid)["Completed"] == True:
        database.TrashFile(taskid)
    else:
        print("Task Not completed!")


@app.command()
def clear(confirmation: bool = False):
    """
    to clear all the task in the to-do-list
    """
    # - temp variable for checking mechanism
    canBeCleared = True

    # - finding all the tasks in the database and storing them in the Tasks
    for task in os.listdir(database.database_path):
        if "Task-" in task:
            index = int(task.split('-')[1].split('.')[0])

            task = database.LoadFile(index)

            # @ - checking mechanism at work
            if task["Completed"] == False:
                canBeCleared = False

            Tasks.append(task)

    # - finalising the checking mechanism
    if canBeCleared or confirmation:
        for task in Tasks:
            database.TrashFile(task["Id"])
    else:
        print("Cannot clear, task are incompleted, or needs confirmation")


@app.command()
def check(times: int):
    "used for checking the program"
    for index in range(times):
        print("Check", "." * index)
    print("Working!")


# ? Implementation
if __name__ == "__main__":
    app()
