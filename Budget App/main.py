"""
STATUS:
OVERVIEW:
IMPROVEMENTS:
Workings:
"""

# @ Imports

# * Defining


class Category:
    def __init__(self, name):
        """ So this functions makes a class a constructor """
        self.categoryName = name.capitalize()
        #  {"amount": amount, "description": description} ledger obj
        self.ledger = []

    def Deposit(self, amount, description=''):
        """ For deposting in the ledger. """
        self.ledger.append({"amount": amount, "description": description})

    def Withdraw(self, amount, description=''):
        """For withdrawing from the ledger. """
        if self.CheckFunds(amount):
            self.ledger.append({"amount": -amount, "description": description})

    def GetBalance(self):
        """ Final amount present. """
        balances = []
        totalAmt = 0

        for entry in self.ledger:
            balances.append(entry['amount'])

        for amt in balances:
            totalAmt += amt

        return totalAmt

    def Transfer(self, category, amount):
        """ Transfer amt from one category instance to another. """
        if self.CheckFunds(amount):
            self.Withdraw(amount, f'Transfered to {category.categoryName}')
            category.Deposit(amount, f'Transfered from {self.categoryName}')

    def CheckFunds(self, amount):
        """ Return True or False if amt can be withdrawn. """
        if amount < self.GetBalance():
            return True
        else:
            print('Funds not availble')
            return False

    def PrintData(self):
        """ Prints category info in a systemised format. """
        # a = ''.ljust()
        print(self.categoryName.center(30, '*'))
        for entry in self.ledger:
            print(
                f"{entry['description'].ljust(23)[:23]}{str(entry['amount']).rjust(7)[:7]}")
        print(f"Total: {self.GetBalance()}")


class Chart:
    def __init__(self, categories):
        """ So this functions makes a class a constructor """
        self.categories = categories

    def FindPercent():
        """ Will find the percent based on ledger. """
        pass


# ? Implementation
if __name__ == "__main__":
    food = Category('food')
    cloth = Category('clotheS')
    food.Deposit(1750, 'Initial Deposit')
    food.Deposit(10, 'Chai ordered')
    food.Withdraw(450, 'Pizza sauce bought')
    food.Transfer(cloth, 700)

    food.PrintData()

