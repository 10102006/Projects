"""
STATUS: Working
OVERVIEW: Gives suggestion to the user on based on the flow
IMPROVEMENTS:
    - Make better suggestions
    - improve `getChunk`
Workings:
# ? Implementation
if __name__ == "__main__":
    s = Suggesttion('08:00', f.flow)
    pp(s.flow)
    print('-----------------------------------------')
    s.suggest()
"""

# @ Imports
from datetime import datetime
from flow import f, setTime
import pprint

pp = pprint.PrettyPrinter(indent=3).pprint
# * Defining


def getTime(strTime):
    return datetime.strptime(strTime, '%H:%M')


def match(time, flow):
    """ """
    for keyAnchor in flow:
        if time == keyAnchor[1]:
            return keyAnchor


class Suggesttion:
    def __init__(self, time, flow):
        self.flow = flow
        self.cTime = time

    def getChunk(self):
        """ """
        fTime = ''
        timeFlow = sorted([getTime(strTime)
                          for _, strTime in self.flow.keys()])

        for time in timeFlow:
            if getTime(self.cTime) > time:
                fTime = setTime(time.hour, time.minute)

        return match(fTime, self.flow)

    def suggest(self):
        """ """
        keyAnchor = self.getChunk()
        events = self.flow[keyAnchor]

        print(f"Lastly at {keyAnchor[1]}, your Keystone Habit is {keyAnchor[0]}:\n")
        for event in events:
            speech = f"Have you done {event.name}?"
            reply = input(f'{speech} (y/n): ').capitalize()
            if reply == 'N':
                print('All the best then!')
                return True
        else:
            print("Okay! Let's move one!")
            return False



