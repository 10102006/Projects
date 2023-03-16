"""
STATUS: Working
OVERVIEW: Gives suggestion to the user on based on the flow.\n
"""
"""
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
from flow import setTime, getTime, match
import pprint
pp = pprint.PrettyPrinter(indent=3).pprint

# * Defining


class Suggestion:
    def __init__(self, time, flow):
        self.flow = flow
        self.currentTime = getTime(time)
        self.timeFlow = sorted([getTime(strTime)
                                for _, strTime in self.flow.keys()])

    def session(self):
        """Full interactive session"""
        check = True
        for i, time in enumerate(self.timeFlow, start=1):
            if check and self.currentTime > self.timeFlow[i]:
                continue

            check = False
            keyAnchor = match(setTime(time.hour, time.minute), self.flow)
            if self.suggest(keyAnchor):
                break
        else:
            print('Welp! Your Scheudle ends here!\n Goodbye!!')

    def suggest(self, keyAnchor):
        """ """
        name, time = keyAnchor
        eventsCycle = self.flow[keyAnchor]

        print(
            f"At {time}, you did {name}:\n" if name else f"At {time}:")

        for event in eventsCycle:
            speech = f"Have you done {event.name}?"
            reply = input(f'{speech} (y/n): ').capitalize()

            if reply == 'N':
                print('-----------------------------------------')
                print(f'All the best with {event.name}!')
                return True
        else:
            print('-----------------------------------------')
            return False


if __name__ == '__main__':
    from database import retrieveSchedule
    f = retrieveSchedule(('schedule')).flow
    s = Suggestion('13:45', f)
    s.session()
