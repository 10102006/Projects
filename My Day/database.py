"""
STATUS: Working
OVERVIEW: Basic Pickle functioning
"""

# @ Imports
import pickle
from pathlib import Path

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

# from flow import f
# saveSchedule('schedule', f)
