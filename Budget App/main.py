"""
STATUS:
OVERVIEW:
IMPROVE:
    - Use decorator for CheckFunds()
    - Make a ledger class
Workings:
"""

# @ Imports

# * Defining


class Category:
    def __init__(self, name):
        """ So this functions makes a class a constructor """
        self.categoryName = name.capitalize()

        self.ledger = [] # data = {"amount": amount, "description": description}

    def Deposit(self, amount, description=''):
        """ For deposting in the ledger. """
        self.ledger.append({"amount": +amount, "description": description})

    def Withdraw(self, amount, description=''):
        """ For withdrawing from the ledger. """
        if self.CheckFunds(amount):
            self.ledger.append({"amount": -amount, "description": description})

    def GetBalance(self):
        """ For presenting the final amount. """
        balances = [entry['amount'] for entry in self.ledger]
        return sum(balances)

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
        """ Prints category info in a systematized format. """
        print(self.categoryName.center(30, '*'))
        for entry in self.ledger:
            # IMPROVE
            description = entry['description'].ljust(23)
            amount = str(entry['amount']).rjust(7)
            print(
                f"{description[:23]}{amount[:7]}")
        print(f"Total: {self.GetBalance()}")

# READ
class Chart:
    def __init__(self, categories):
        self.categories = categories
        self.FindSpentPercent()
        # self.View()

    def FindSpentPercent(self):
        """ Will find how much spending each category has done based on ledger. """
        self.percentTable = {}
        grandTotalSpent = 0

        for category in self.categories:
            totalSpent = 0

            for entry in category.ledger:
                if entry['amount'] < 0: # means a expenditure
                    totalSpent += entry['amount']
                    grandTotalSpent += entry['amount']

            self.percentTable.update({category.categoryName: totalSpent})

        for category, amount in self.percentTable.items():
            self.percentTable[category] = round(
                (amount/grandTotalSpent) * 10, 0)


    def Graph(self):
        """ """
        keys = ['']

        # Makes a 11 X 5 Graph
        graph = [
            [' ' for _ in range(5)]
                 for _ in range(11)
        ]

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

    food.Deposit(1750, 'Initial Deposit')
    cloth.Deposit(2510, 'Initial Deposit')

    food.Withdraw(150, 'Pizza bought')
    cloth.Withdraw(520, 'Pizza hat bought')

    food.Transfer(cloth, 300)
    cloth.Transfer(food, 550)
    chart = Chart([food, cloth])
    chart.Graph()

"""
    food.PrintData()
    cloth.PrintData()

    room = Category('ROOM')
    room.Deposit(2280, 'Initial Deposit')
    room.Withdraw(450, 'Pizza sauce bought')
    room.Withdraw(450, 'Pizza sauce bought')
    cloth.Transfer(room, 100)
"""
