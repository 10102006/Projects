"""
STATUS: Working
OVERVIEW: controls the flow of the events happening
IMPROVEMENTS:
    - better `append()`
    - make it more streamlined, meaning not broken but to work as a single unit
    - implement preiod system
"""

# @ Imports
from datetime import time, datetime

# * Defining


def setTime(hour, minute=0):
    """returns a `str` obj for given hour and minutes."""
    return time(hour, minute).strftime('%H:%M')


def getTime(strTime):
    """returns a `time` for given str"""
    return datetime.strptime(strTime, '%H:%M')


def match(time, flow):
    """Get `keyAnchor` of matching time."""
    for keyAnchor in flow:
        if time == keyAnchor[1]:
            return keyAnchor


class Flow():
    def __init__(self, events):
        self.flow = {
            ('wake up', setTime(5)): [],
            ('study', setTime(16)): [],
            ('sleep', setTime(23)): []
        }
        self.events = list(events)

        self.sync()

    def sync(self, events=None):
        """ """
        if events:
            self.events = events

        for _ in self.events:
            self.initialise()
            self.append()
            self.reiterate()

    def initialise(self):
        """ """
        for keyAnchor in (self.flow):
            for event in (self.events):
                if event.anchor == keyAnchor[0]:
                    self.flow[keyAnchor].append(event)
                    self.events.remove(event)

    def append(self):
        """ """
        counter = 0
        while counter < max((len(events) for events in self.flow.values())):
            for keyAnchor in self.flow.keys():

                if len(self.flow[keyAnchor]) <= counter:
                    continue

                for event in (self.events):
                    newAnchor = self.flow[keyAnchor][counter]

                    if event.anchor == newAnchor.name:
                        self.flow[keyAnchor].append(event)
                        self.events.remove(event)

            counter += 1

    def reiterate(self):
        """ """
        for event in self.events:
            if ':' in event.anchor:
                self.flow[('', event.anchor)] = [event]
                self.events.remove(event)


class Event():
    def __init__(self, name, anchor, period=''):
        self.name = name
        self.anchor = anchor
        # self.period = period

    def get(self):
        return self.__dict__


# ? Implementation
if __name__ == '__main__':

    evnts = [
        Event('exercise', 'wake up'),
        Event('draw', 'exercise'),

        Event('code', 'study'),

        Event('brush', '22:00'),
        Event('jornal', 'brush'),
        Event('draw', 'jornal')
    ]

    f = Flow(evnts)

# for event in f.flow:
#     print(event)
#     pp(f.flow[event])
#     print('-----------------------------------------')
