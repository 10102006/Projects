
"""
STATUS: Wokring(not fully)
OVERVIEW: Is the control unit of the program
IMPROVEMENTS:
Workings:
    - Incomplete
"""

# @ Imports
import argparse
import flow
import suggestions
import database
import pprint
pp = pprint.PrettyPrinter(indent=3).pprint

# * Defining
# parser = argparse.ArgumentParser(description='Helpful tool for scheduling and managing ones day.')

# parser.add_argument('command', type=str, help='what to do?')
# args = parser.parse_args()

scheduleName = 'my schedule'
scheduleFlow = database.retrieveSchedule(scheduleName)


def Show():
    """ """
    schedule = scheduleFlow.flow

    def keyTime(keyAnchor):
        return suggestions.getTime(keyAnchor[1])

    keyAnchors = sorted(schedule.keys(), key=keyTime)

    for keyAnchor in keyAnchors:
        print(f"/* {keyAnchor[0]} at {keyAnchor[1]}")
        for event in schedule[keyAnchor]:
            print(f"\t/ {event.name} after {event.anchor}")


def AddEvent(scheduleFlow):
    print('--- Defined Habits ---')
    eventName = input("Enter new habit name: ")
    eventAnchor = input('Enter new Anchor: ')

    event = flow.Event(eventName, eventAnchor)

    scheduleFlow.events.append(event)
    scheduleFlow.sync()


def SaveChanges():
    database.saveSchedule(scheduleName, scheduleFlow)


def ChangeKeyAnchor(scheduleFlow):
    """ """
    print(f'--- Mandatory Events ---')
    keyAnchor = [_keyAnchor for _keyAnchor in scheduleFlow.flow.keys()
                 if _keyAnchor[0]][2]
    # for keyAnchor in scheduleFlow.flow.keys():
    newTime = input(f'when to {keyAnchor[0]}(previous: {keyAnchor[1]}): ')
    newTime = '{:02d}:{:02d}'.format(*[int(s) for s in newTime.split(':')])

    scheduleFlow.flow.update(
        {(keyAnchor[0], newTime): scheduleFlow.flow[keyAnchor]})
    scheduleFlow.flow.pop(keyAnchor)


# ? Implementation

if __name__ == "__main__":
    ChangeKeyAnchor(scheduleFlow)
    Show()

    s = suggestions.Suggesttion('18:30', scheduleFlow.flow)
    s.suggest()

# if args.command == 'show':
    #    print('Hello World!')
