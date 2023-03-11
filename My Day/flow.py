"""
STATUS:
OVERVIEW:
IMPROVEMENTS:
Workings:
"""

# @ Imports

# * Defining


class Flow():
    def __init__(self, events):
        self.flow = {
            ('wake up', '05:00'): [],
            ('study', '16:00'): [],
            ('sleep', '23:00'): []
        }
        self.events = events

        self.initialise()
        self.sync()
        self.reiterate()

        print(self.flow)

    def sync(self):
        """ """
        counter = 0
        print(len(self.events))
        while counter < 100:
            for keyAnchor in self.flow.keys():
                for event in (self.events):
                    try:
                        if event.anchor == self.flow[keyAnchor][counter].name:
                            self.flow[keyAnchor].append(event)
                            self.events.remove(event)
                    except:
                        pass
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
            self.flow[('', event.anchor)] = [event]


class Event():
    def __init__(self, name, anchor, period):
        self.name = name
        self.anchor = anchor
        self.period = period


# ? Implementation
evnts = [
    Event('exercise', 'wake up', 30),
    Event('draw', 'exercise', 30),
    Event('brush', '22:00', 10),
    Event('code', 'study', 120)
]

if __name__ == "__main__":
    f = Flow(evnts)
