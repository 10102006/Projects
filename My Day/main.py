
"""
STATUS: Wokring
OVERVIEW: Is the control unit of the program
IMPROVEMENTS:
    - make a seprate argparse file
WORKINGS:
    - Implement multiple system
    - Add suggestions
"""

# @ Imports
import datetime
import argparse
import flow
import suggestions
import database

# * Defining
TIME = datetime.time(hour=15).strftime("%H:%M")
SCHEDULENAME = 'schedule'
SCHEDULE = database.retrieveSchedule(SCHEDULENAME)

# * Argparse
PARSER = argparse.ArgumentParser(
    description='Helpful tool for scheduling and managing ones day.')

PARSER.add_argument('command', type=str,
                    help='available commands: show, add, change', choices=['show', 'add', 'change'])
PARSER.add_argument('-data', '-d', type=str,
                    help='available input: habit and KA', choices=['habit', 'key anchor'])
PARSER.add_argument('-multiple', '-m', action='store_true')

args = PARSER.parse_args()


class MyDay:
    def __init__(self):
        self.scheduleFlow = SCHEDULE.flow
        self.keyAnchors = self.get_keyAnchors()

    def get_keyAnchors(self):
        """ returna a sorted list of the `keyAnchors`. """
        return sorted(self.scheduleFlow.keys(
        ), key=lambda keyAnchor: suggestions.getTime(keyAnchor[1]))

    def show(self):
        """ prints the `flow` in a hierachy. """
        for name, time in self.get_keyAnchors():
            print("/*", name,  'at', time)

            keyAnchor = (name, time)
            for event in self.scheduleFlow[keyAnchor]:
                print(f"\t/ {event.name} after {event.anchor}")

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


# ? Implementation
if __name__ == "__main__":
    main = MyDay()

    if args.command == 'show':
        main.show()
        quit()

    try:
        func = Add if args.command == 'add' else Change
        if args.data == 'habit':
            func.event()
        elif args.data == 'key anchor':
            func.keyAnchor()
        else:
            raise Exception('INCOMPLETE PROMPT: enter data to alter using (-d)')

        main.save()
    except Exception as e:
        print(e)

