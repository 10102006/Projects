TODO clean this shit

What all can be done:
   1. init => initializing the home database
   2. list => viewer which will display the to do list

      To-Do List: Date

      ID.   | Name   | Pri | Done | Description
      ----- | ------ | --- | ---- | ---------------
      1.    |        |     |      |
      2.    |        |     |      |
      3.    |        |     |      |

   3. add(taskName, taskPriority=3, taskDescription=taskName) => this will add tasks to the list
   4. complete(taskId) => this is mark the task as completed
   5. remove(taskId) => this will remove the task after confirmation
   6. clear => whole list cleared after confirmation

Database:
   - make an instance of {Database} class => database = Database(database_path)
   - make an id enumerator => Id = TaskId(database_path)
                              id = iter(Id)
   - make a task in dict format
   - save the task using => database.SaveFile(task)
   - retrieve the task using => r_task = database.LoadFile(taskId)
   - #check the task using => database.ChangeFile(taskId)
   - delete the task using => database.TrashFile(taskId)
   - clean Trash folder => database.CleanTrash(True if input("Clean Trash y/n: ") == 'y' else False)

Viewer:
   - make an instance of {Table} class => toDoTable = Table(titles)
   - make an instance of {Display} class => display = Display(toDoTable)
   - add task to the table using => toDoTable.AddToTable(task)
   - print the table using => display.PrintTable()

##  Test for save the tasks
~~~
    # Tasks = [
    #     Task(name=f"{index}-task",
    #          id=next(id),
    #          priority=2,
    #          description=f"Test task {index}") for index in range(5)
    # ]
~~~
## For task in Tasks:
~~~
    #     database.SaveFile(task)

    # * - test for retrieving the tasks
    # for task in os.listdir(database.database_path):
    #     if "Task-" in task:
    #         index = int(task.split('-')[1].split('.')[0])

    #         task = database.LoadFile(index)
    #         Tasks.append(task)
~~~
## For changing the tasks
~~~
    # database.ChangeFile(1)

    # * - test for trashing the tasks
    # database.TrashFile(1)

    # for task in os.listdir(database.database_path):
    #     if "Task-" in task:
    #         index = int(task.split('-')[1].split('.')[0])

    #         task = database.LoadFile(index)
    #         Tasks.append(task)
~~~
~~~
    # [print(task) for task in Tasks]

    # * - test for table formation
    # for task in Tasks:
    #     toDoTable.AddToTable(task)

    # display.PrintTable()

~~~
