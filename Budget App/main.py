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
        self.FindPercent()
        self.View()

    def FindPercent(self):
        """ Will find the percent based on ledger. """
        self.percentTable = {}
        grandTotal = 0
        for category in self.categories:
            totalSpent = 0
            for entry in category.ledger:
                if entry['amount'] < 0:
                    totalSpent -= entry['amount']
                    grandTotal -= entry['amount']
            self.percentTable.update({category.categoryName: totalSpent})

        for val in self.percentTable:
            self.percentTable[val] = int(round(
                (self.percentTable[val]/grandTotal) * 10, 0))

    def Graph(self):
        """ """
        keys = ['']
        graph = []
        for pi in range(11):
            graph.append([' ' for _ in range(5)])

        for ri, row in enumerate(graph):
            for ci, pi in enumerate(self.percentTable.values(), start=1):
                if 9-pi < ri:
                    graph[ri][ci] = 'o'
            graph[ri][0] = f"{(10-ri) * 10} |".rjust(5)

        for key in self.percentTable.keys():
            vl = ''
            for char in key:
                vl = vl + f"\n{char}"
            keys.append(vl)

        for row in graph:
            print(*row)

    def WordOrient(self):
        """ """
        keys = list(self.percentTable.keys())

        longest = len(keys[0])
        for key in keys:
            if len(key) > longest:
                longest = len((key))

        tb = [['-' for _ in keys]]
        for _ in range(longest):
            tb.append(['' for _ in keys])

        for ri, row in enumerate(tb):
            for ci, key in enumerate(row):
                try:
                    char = keys[ci][ri]
                except:
                    pass
                else:
                    pass
                    tb[ri+1][ci] = char

        for i in tb:
            print(' ' * 5, *i)

    def View(self):
        """ """
        print("Percent Spent by Category")
        self.Graph()
        self.WordOrient()


# ? Implementation
if __name__ == "__main__":
    food = Category('food')
    cloth = Category('clotheS')
    room = Category('ROOM')
    food.Deposit(1750, 'Initial Deposit')
    room.Deposit(2280, 'Initial Deposit')
    cloth.Deposit(2510, 'Initial Deposit')

    food.Withdraw(150, 'Pizza sauce bought')
    room.Withdraw(450, 'Pizza sauce bought')
    room.Withdraw(450, 'Pizza sauce bought')
    cloth.Withdraw(520, 'Pizza sauce bought')
    food.Transfer(cloth, 300)
    food.Transfer(cloth, 300)
    food.Transfer(cloth, 300)
    food.Transfer(cloth, 300)
    food.Transfer(cloth, 300)
    cloth.Transfer(room, 100)

    food.PrintData()
    print()
    room.PrintData()
    print()
    cloth.PrintData()
    print()

    chart = Chart([food, room, cloth])
