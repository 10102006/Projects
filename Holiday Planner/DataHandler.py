"""
STATUS: Working

OVERVIEW: JSON format handler of State

IMPROVEMENTS:
    - Find out about classes

"""


# * Defining
class State:
    """
    Handles the State related function also works as a complier
    """

    def __init__(self, name, description, touristPlaces):
        """
        Initialisign Name, Details and Empty TouristPlaces.0
        """
        self.Name = name
        self.Description = description
        self.TouristPlaces = touristPlaces

    @classmethod
    def Create(cls):
        """
        CLI for making a State
        """
        Name = input("Enter State Name: ")
        Description = input("Enter State Description: ")
        TouristPlaces = []

        for _ in range(int(input("How many Tourist Places to Create: "))):
            TouristPlaces.append(TouristPlace.Create())

        return cls(Name, Description, TouristPlaces)

    def AddTouristPlace(self, touristPlace):
        """
        This will append the touristPlace to the state
        and then add the state object will be added to the main dict with the name given
        """
        self.TouristPlaces.append(touristPlace)

    def GetState(self):
        """
        Returning in Dictionary Format
        """
        State = self.__dict__
        State['TouristPlaces'] = [touristPlace.__dict__ for touristPlace in State['TouristPlaces']]
        return State


class TouristPlace:
    def __init__(self, name, description, hotels, transports):
        """
        Initialising Name, Details, Hotels and Transports
        """
        self.Name = name
        self.Description = description
        self.Hotels = hotels
        self.Transports = transports

    @classmethod
    def Create(cls):
        """
        CLI for creating a Tourist Place
        """
        Name = input('Enter Name of the Tourist Place: ')
        Description = input('Enter Description of the Tourist Place: ')
        Hotels = []
        Transports = []

        for _ in range(int(input('How many hotels to add: '))):
            name = input('Hotel name: ')
            rating = int(input('Hotel rating(number): '))
            price = int(input('Hotel price(number): '))

            hotel = (name, rating, price)
            Hotels.append(hotel)

        for _ in range(int(input('How many transports to add: '))):
            name = input('Transport name: ')
            price = int(input('Transport price(number): '))

            transport = (name, price)
            Transports.append(transport)

        return cls(Name, Description, Hotels, Transports)

    def AddHotel(self, hotel=tuple):
        """
        Add hotel to the database
        """
        self.Hotels.append(hotel)

    def AddTransport(self, transport=tuple):
        """
        Adding transport the database
        """
        self.Transports.append(transport)


touristPlaces = [
TouristPlace(
    'yo' * i,
    'ha'*i*3,
    [
    ('a', 1, 12), ('b', 5, 12345)
    ],
    [
    ('as', 45), ('qw', 78)
    ]
) for i in range(3)
]

cg = State('CG', 'LOL', touristPlaces)
print(cg.GetState())
