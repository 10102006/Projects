"""
STATUS:
OVERVIEW:
IMPROVEMENTS:
Workings:
"""

# @ Imports
import pickle
from pathlib import Path
from flow import f

PATH = Path.cwd() / 'Database'

# * Defining


def saveSchedule(scheduleName, flow):
    try:
        with open(PATH / f'{scheduleName}.pickle', 'wb') as file:
            pickle.dump(flow, file, pickle.HIGHEST_PROTOCOL)
    except Exception as e:
        print(e)


def retrieveSchedule(scheduleName):
    try:
        with open(PATH / f'{scheduleName}.pickle', 'rb') as file:
            return (pickle.load(file))
    except Exception as e:
        print(e)


# ? Implementation
if __name__ == "__main__":
    print(retrieveSchedule('my schedule'))
    # (saveSchedule('my schedule', f))
