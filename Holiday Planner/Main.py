"""
STATUS: Unknown

OVERVIEW: Check

IMPROVEMENTS:

TODO Break down it into seperate files

State - fldr
{
    details:'',
    tourist_places :
    {
        tourist_place: - fldr
        {
            description: 'string',
            transports: [list of transports],
            hotels: - fldr
            {
                hotel:[ratings, price_of_stay],
            }
        },
        tourist_place: - fldr
        {
            description: 'string',
            transports: [list of transports],
            hotels: - fldr
            {
                hotel:[ratings, price_of_stay]
            }
        },
    }
}


"""

# * Imports
import os
from os import path
import JSONState as Dict_State
import FileHandler as File_State

# @ Definition


class CLI(Dict_State):
    """
    How it should work:

    1. Which state do you want to visit => [list of states]
        1. Print description
        2. Confirm => Using the Recursive Function
    2. Which tourist place do you want to visit => [list of tourist places]
        1. Print description
        2. Confirm
        3. Tell transports => [list of transports]
            1. Confirm
        4. Which hotel do you want to vist => [list of hotel names]
            1. Print Ratings
                1. Confirm
            2. Print Price
                1. Confirm
            3. Confirm
    """

    def __init__(self, main_database):
        self.database = main_database

    def Choose_From_List(self, p_list, placeholder_txt='Which item do you want(enter index no or name): ',symbol='.'):
        """
        """
        m_list = [item for item in p_list]
        for index, item in enumerate(m_list, 1):
            printed_str = (f'{index}{symbol} {item}')
            print(printed_str)

        print('-----------------------------------------------------')
        choosen_item = input(placeholder_txt)
        r_item = ''

        try:
            if choosen_item.isnumeric():
                r_item = m_list[int(choosen_item) - 1]
            elif choosen_item in m_list:
                r_item = choosen_item
        except:
            print('Soory some error!')
            self.Choose_From_List(p_list, placeholder_txt, symbol)
        else:
            print('-----------------------------------------------------')
            print(r_item)
            print('-----------------------------------------------------')

            confirm = True if input('Do you chose above item (Y/N): ').capitalize() == 'Y' else False
            if confirm:
                print('-----------------------------------------------------')
                return r_item
            else:
                self.Choose_From_List(p_list, placeholder_txt, symbol)

            return r_item

    def Main(self, main_database):
        """
        """
        state_name = self.Choose_From_List(main_database.keys())

        state = main_database.get(state_name)
        state_details = state.get('details')

        print('details: ' + state_details)

        main_touristplace = state.get('tourist_places')
        tourist_place_name = self.Choose_From_List(main_touristplace.keys())

        tourist_place = main_touristplace.get(tourist_place_name)
        tourist_place_description = tourist_place.get('description')
        print('Description: ' + tourist_place_description)

        transports_list = tourist_place.get('transports')
        transport = self.Choose_From_List(transports_list)

        main_hotels = tourist_place.get('hotels')
        hotel_name = self.Choose_From_List(main_hotels.keys())

        hotel = main_hotels.get(hotel_name)
        ratings, price = hotel[0], hotel[1]

        print('Ratings of hotel' + str(hotel_name) + 'are: ' + ratings)
        print('Prices of hotel' + str(hotel_name) + 'are: ' + price)

        confirm = True if input('Do you accept the hotel? (Y/N): ').capitalize() == 'Y' else False
        if confirm:
            ticket = self.Make_Ticket(hotel_name, hotel, tourist_place_name, transport, state_name)

            return ticket
        else:
            self.Main(main_database)

    @staticmethod
    def Make_Ticket(name_hotel, hotel, name_tourist_place, transport, name_state):
        """
        width = 94
        hieght = 10
        """
        ticket_obj = {}
        ticket_obj.update({name_state:{}})

        tourist_place = {"transport":transport, name_hotel:hotel}

        t_state = ticket_obj.get(name_state)
        t_state.update({name_tourist_place:tourist_place})

        return ticket_obj

    @staticmethod
    def Print_Ticket(ticket):
        """
        """
        ticket_line = f'{"-" * 90}'

        def print_line(line, line_width=92):
            """
            """
            gap = ' ' * ((line_width - 2) - len(line))
            t_line = '|' + str(line) + gap + '|'
            print(t_line)

        def get_first(lst, sh=False):
            """
            """
            _lst = [item for item in lst]
            return _lst if sh else _lst[0]

        print_line(ticket_line)
        print_line('')

        state = get_first(ticket.keys())
        print_line('    State: ' + state)
        touristplace = get_first(ticket.get(state).keys())
        print_line('    Tourist place: ' + touristplace)

        print_line('')

        # lst =[]

        hotel = get_first(ticket.get(state).get(touristplace).keys(), True).pop(1)
        print_line('    Hotel: ' + hotel)
        transport = ticket.get(state).get(touristplace).get('transport')
        print_line('    Transport: ' + transport)

        print_line('')

        price = ticket.get(state).get(touristplace).get(hotel)[1]
        print_line('    Price: ' + price)
        print_line(ticket_line)

# ? Implementation

if __name__ == "__main__":
    Database = {}

    cli = CLI(Database)
    init = Dict_State()
    file = File_State('E:\Coding & Bowsers\Python Codes\Projects\Holiday Planner\Database')

