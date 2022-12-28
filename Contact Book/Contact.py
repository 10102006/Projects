"""
STATUS: Working

OVERVIEW: For generating contacts

IMPROVEMENTS:
    - TODO Implement Group
"""

# * Defining


class Contact:
    def __init__(self, alias, number):
        """
        Initialising Name, PhoneNumbers and Email
        """
        self.Alias = [alias]
        self.PhoneNumbers = [number]
        self.Email = ''
        # self.Group

    def Update(self, info, value):
        """
        Updating the contact info.
        """
        match (info, value):
            case ('Alias', name):
                if isinstance(name, list):
                    self.Alias = name
                else:
                    self.Alias.append(name)
            case ('PhoneNumbers', numbers):
                if isinstance(numbers, list):
                    self.PhoneNumbers = numbers
                else:
                    self.PhoneNumbers.append(numbers)
            case ('Email', email):
                self.Email = email

    def get(self):
        return self.__dict__
