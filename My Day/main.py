
"""
STATUS: Wokring
OVERVIEW: Is the control unit of the program
IMPROVEMENTS:
    - make a seprate argparse file
WORKINGS:
    - Add suggestions
"""

# @ Imports
import datetime
import flow
from flow import getTime
from suggestions import Suggestion
import database

# * Defining
TIME = datetime.datetime.now().strftime("%H:%M")
SCHEDULENAME = 'schedule'
SCHEDULE = database.retrieveSchedule(SCHEDULENAME)



class MyDay:
    def __init__(self):
        self.scheduleFlow = SCHEDULE.flow
        self.keyAnchors = self.get_keyAnchors()

    def get_keyAnchors(self):
        """ returna a sorted list of the `keyAnchors`. """
        return sorted(self.scheduleFlow.keys(
        ), key=lambda keyAnchor: getTime(keyAnchor[1]))

    def show(self):
        """ prints the `flow` in a hierachy. """
        for name, time in self.get_keyAnchors():
            print("/*", name,  'at', time)

            keyAnchor = (name, time)
            for event in self.scheduleFlow[keyAnchor]:
                print(f"\t/ {event.name} after {event.anchor}")

    def suggest(self):
        """ """
        suggestion = Suggestion(TIME, SCHEDULE.flow)
        suggestion.session()

    def save(self):
        try:
            database.saveSchedule(SCHEDULENAME, SCHEDULE)
        except Exception as e:
            print(e)

    @staticmethod
    def promptTo(function, data):
        """ """
        title = 'Adding' if function == 'add' else 'Changing'
        descriptor = 'anchor' if data == 'habit' else 'time'

        print(f"--- {title} {data.capitalize()} ---")

        _firstPrompt = input(f'Enter name of the {data} : ')
        _secondPrompt = input(
            f'Enter the {descriptor}: ')

        return _firstPrompt, _secondPrompt


class Add(MyDay):
    @staticmethod
    def event():
        name, anchor = MyDay.promptTo('add', 'habit')

        try:
            event = flow.Event(name, anchor)

            SCHEDULE.events.append(event)
            SCHEDULE.sync()
        except Exception:
            print("Wrong Input!")

    @staticmethod
    def keyAnchor():
        name, time = MyDay.promptTo('add', 'key anchor')
        time = '{:02d}:{:02d}'.format(
            *[int(value) for value in time.split(':')])

        try:
            SCHEDULE.flow[(name, time)] = []
            SCHEDULE.sync()
        except Exception:
            print("Wrong Input!")


class Change(MyDay):
    @staticmethod
    def event():
        name, anchor = MyDay.promptTo('change', 'habit')

        try:
            for event in SCHEDULE.events:
                if event.name == name:
                    event.anchor = anchor
        except Exception as e:
            print("Given habit doesn't exist!")

    @staticmethod
    def keyAnchor():
        name, time = MyDay.promptTo('change', 'key anchor')
        time = '{:02d}:{:02d}'.format(
            *[int(value) for value in time.split(':')])

        for _anchorName, _time in SCHEDULE.flow.keys():
            if _anchorName == name:
                anchor = (_anchorName, _time)

        try:
            SCHEDULE.flow[(name, time)] = SCHEDULE.flow[anchor]
            SCHEDULE.flow.pop(anchor)

            SCHEDULE.sync()
        except Exception:
            print("Given Key Anchor doesn't exist!")
