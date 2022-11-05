## Basic overview
   1. This can tell me what to do at the time of usage
   2. Will store my day's schedule in a json format
   3. Can help in changing my schedule
   4. Can show me my schedule
   5. This will also give a reminder if need be
   6. Time which is not alloted will be termed as free time

## My schedule's look:

| Index | StartingTime | EndingTime | Name... |
| ----- | ------------ | ---------- | ------- |
| 1     | 10:00:00     | 11:00:00   | Break   |
| 2     | 13:00:00     | 13:30:00   | Skills  |
| 3     | 20:00:00     | 22:00:00   | Novel   |
| 5     | 12:45:00     | 13:45:00   | Jogging |

## Code Functionality

1. **Handler**: This file is taking care of kinda the backend of the project, so like the database handling and shit.

   - Database: is the main class containing all the functions, this will take care of directory changing.
     - CreateSlot(name, startingTime, endingTime): is used for creating a slot dict obj for data storage.
     - SaveSlot(slotObject): uses the json module to save the slot obj made in a json file format.
     - LoadSlot(filename): uses the json module to extract the data saved in a specific file of name ```filename```.
     - SetIndex(slotObject): checks where the slot would fit in the schedule and then finds an appropriate index.
     - AdjustSlot(slotObject): is helpful in rearranging the slots according to there time-stamp.

``` python
    database = Database(database_path)

    # Single unique slot
    slot = database.CreateSlot("Jogging", (12, 32))

    # Saving the unique slot
    database.SaveSlot(slot)

    # Retrieving the Saved slot
    slot = database.LoadSlot(slot["Index"])

    # Placeholder slots
    for index in range(5):
        slot = database.CreateSlot(f"Task-{index}", (10 + index * 2, 0))
        database.SaveSlot(slot)

    # Rearranging the slots to accommodate the new slot
    database.AdjustSlot(slot)
```

---

***
1. **Viewer**: This file is like a front-end of the project as it is taking care of the viewer of the stuff.
    - Schedule(path, slots): is the main class containing all the function for viewing our schedule. ```slots``` will contain all the slots we have saved, this class will turn it into a ```schedule``` object
      - MakeSchedule(): will add the items to there respective key in ```schedule``` object.
      - PrintSchedule(schedule): will print all the schedule in the above mentioned format.

``` python
    scheduleManager = Schedule(database_path, Slots)

    #  Making a schedule
    schedule = scheduleManager.MakeSchedule()

    # Printing the Schedule
    scheduleManager.PrintSchedule(schedule)
```

---

***
1. **Main**
