"""
STATUS: Working

OVERVIEW: JSON format handler of State

IMPROVEMENTS:
    - Find out about classes

"""


# * Defining
class STATE:
    """
    Handles the State related function also works as a complier
    """

    def __init__(self, name="", details=""):
        """
        Initialisign Name, Details and Empty TouristPlaces.0
        """
        self.Name = name if name else input("Enter the State name: ")
        self.Details = details if details else input("Enter the State details: ")

        self.TouristPlaces = []

    def AddTouristPlace(self, touristPlace):
        """
        This will append the touristPlace to the state
        and then add the state object will be added to the main dict with the name given
        """
        self.TouristPlaces.append(touristPlace.__dict__)

    def GetState(self):
        """
        Returning in Dictionary Format
        """
        return self.__dict__


class TOURISTPLACE:
    def __init__(self, name="", details=""):
        """
        Initialising Name, Details, Hotels(empty) and Transports(empty)
        """
        self.Name = name if name else input("Enter name of the Tourist Place: ")
        self.Details =details if details else input("Enter details of the Tourist Place: ")

        self.Hotels = []
        self.Transports = []

    def MakeHotels(self, name=None, rating=None, price=None):
        """
        CLI snippet for making hotels objects
        """
        if price != None:
            hotel = (name, rating, price)
            self.Hotels.append(hotel)

        else:
            for _ in range(int(input("How many hotels would your like to make: "))):
                hotel = (
                    input("Enter the name of the Hotel: "),
                    input("Enter the rating of the Hotel: "),
                    input("Enter the price of stay at the hotel: "),
                )
                self.AddHotel(hotel)
                print("-----------------------------------------")

    def AddHotel(self, hotel):
        """
        Add hotel to the list
        """
        self.Hotels.append(hotel)

    def AddTransport(self, transport):
        """
        List of transportation available.
        """
        self.Transports.append(transport)
