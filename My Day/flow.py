"""
STATUS: Working
OVERVIEW: controls the flow of the events happening
IMPROVEMENTS:
    - better `append()`
    - make it more streamlined, meaning not broken but to work as a single unit
    - implement preiod system
"""

# @ Imports
import pprint
pp = pprint.PrettyPrinter(indent=4, width=1).pprint

# * Defining


class Flow():
    def __init__(self, events):
        self.flow = {
            ('wake up', '05:00'): [],
            ('study', '16:00'): [],
            ('sleep', '23:00'): []
        }
        self.events = list(events)

        self.sync()

    def sync(self, events=None):
        """ """
        if events:
            self.events = events

        self.initialise()
        self.append()
        self.reiterate()

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

    def initialise(self):
        """ """
        for keyAnchor in (self.flow):
            for event in (self.events):
                if event.anchor == keyAnchor[0]:
                    self.flow[keyAnchor].append(event)
                    self.events.remove(event)

    def reiterate(self):
        """ """
        for event in self.events:
            if ':' in event.anchor:
                self.flow[('', event.anchor)] = [event]


class Event():
    def __init__(self, name, anchor, period=''):
        self.name = name
        self.anchor = anchor
        # self.period = period

    def get(self):
        return self.__dict__


# ? Implementation
evnts = [
    Event('exercise', 'wake up'),
    Event('draw', 'exercise'),
    Event('brush', '22:00'),
    Event('code', 'study'),
    Event('jornal', 'brush'),
    Event('draw', 'jornal')
]

if __name__ == "__main__":
    f = Flow(evnts)
    pp(f.flow)
