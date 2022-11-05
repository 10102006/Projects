"""
STATUS:
OVERVIEW:
IMPROVEMENTS:
Workings:

STATE: /fdr
{
    - TOURIST PLACES: /fdr
    {
        CITY: /fdr
        {
            HOTELS: /fdr
            {
                HOTELS: File containing hotel details
            }
            DETAILS: About the city.
            TRANSPORTS: List of transports avail
        }
    }
    - DETAILS: Explains the state.
}


"""

# @ Imports
import os
from os import path, scandir, chdir
from os.path import join
import json

import DataHandler as dh

root = r"E:\Coding\Projects\Holiday Planner\Database"

# * Defining
class DUMP:
    """
    Handler for making a folder tree of State object
    """

    def __init__(self, root=""):
        self.root = path.join(root)
        os.chdir(self.root)

    def State(self, State):
        """
        Generates folders operates other functions of class.
        """
        os.makedirs(f"{State['Name']}/TouristPlaces", exist_ok=True)
        chdir(f"./{State['Name']}")
        with open("Details.txt", "w") as file:
            file.write(State["Details"])

        for touristPlace in State.get("TouristPlaces"):
            chdir(join(self.root, f"{State['Name']}/TouristPlaces"))
            self.TouristPlace(touristPlace)

            chdir(f"./Hotels")
            [self.Hotel(hotel) for hotel in touristPlace["Hotels"]]

    def TouristPlace(self, place):
        """
        Generates folders and files of tourist place dict.
        """
        name, details, _, transports = place.values()

        os.makedirs(f"{name}//Hotels")
        chdir(join(name))

        for item in place:
            text = ""
            if item == "Details" or item == "Transports":
                match item:
                    case "Details":
                        text = details
                    case "Transports":
                        text = "\n".join(transports)

                with open(f"{item}.txt", "w") as file:
                    file.write(text)

    def Hotel(self, hotel):
        """
        Generates a hotel file containing its details
        """
        name, rating, price = hotel

        with open(f"{name}.txt", "w") as hotel:
            hotel.write(f"{name} has a good rating of {rating}" + "\n")
            hotel.write(f"{name}'s price of stay is {price}/night" + "\n")


class SQLHandler:
    pass


# ? Implementation
if __name__ == "__main__":
    cg = dh.STATE(
        "Chhattisgarh",
        "A relative backwards state of India has a great potential for providing human resource.",
    )

    tps = []
    for i in range(3):
        tp = dh.TOURISTPLACE(f"Tourist Place-{i + 1}", "lorem ipsum dore")
        [
            tp.AddTransport(transport)
            for transport in ["car", "train", "airplane", "ship"]
        ]
        [
            tp.MakeHotels(f"{f + 1} Hotel", (f + 1) * 2, (f + 1) * 320)
            for (f) in range(3)
        ]

        tps.append(tp)

    [cg.AddTouristPlace(touristPlace) for touristPlace in tps]

    print(json.dumps(cg.GetState(), indent=2))

    dump = DUMP(root)
    dump.State(cg.GetState())
