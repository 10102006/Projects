"""
STATUS: Working

OVERVIEW: Basically adding and subtracting of string operations

IMPROVEMENTS:
    - Shit ton of!
    - TODO Document
Workings:
"""

# @ Imports
import re

# * Defining


class Operation:
    """ Will handle each operation as an object """

    def __init__(self, operation, solve=False):
        """
            So this functions makes a class a constructor
        """
        self.operation = operation
        self.solve = solve

        self.operation_splitter()
        self.string_beautifier()

    def operation_splitter(self):
        """ Will format the string and return num1, num2 and operator """
        operands = re.split('\s', self.operation)
        self.num1 = operands[0]
        self.operation = operands[1]
        self.num2 = operands[2]

        if not self.num1.isalnum() or not self.num2.isalnum():
            raise Exception('Numbers must only contain digits.')

        if self.operation != '+' and self.operation != '-':
            raise Exception("Operator must be '+' or '-'.")

        if self.operation == '+':
            self.soln = int(self.num1) + int(self.num2)
        else:
            self.soln = int(self.num1) - int(self.num2)

    def string_beautifier(self):
        """ """
        self.maxLen = len(
            self.num1)+2 if len(self.num1) > len(self.num2) else len(self.num2)+2

        if self.maxLen > 6:
            raise Exception('Numbers cannot be more than four digits.')

        self.r1 = self.num1.rjust(self.maxLen)
        self.r2 = f'{self.operation} {self.num2.rjust(self.maxLen - 2)}'
        self.soln = str(self.soln).rjust(self.maxLen)

    def printable(self):
        """ """
        if self.solve:
            return (self.r1, self.r2, self.maxLen, self.soln)
        return (self.r1, self.r2, self.maxLen)


class Viewer:
    """ Print the output """

    def __init__(self, printables):
        """ So this functions makes a class a constructor """
        self.printables = printables
        # TODO  Make a rows list
        self.r1 = ''
        self.r2 = ''
        self.r3 = ''
        self.r4 = ''

        if len(printables) > 5:
            raise Exception('Too many problems.')

        self.arranger()

    def arranger(self):
        """ Will arrange all the item of a list in a single string """
        for printable in self.printables:
            self.r1 = self.r1 + printable[0] + '    '
            self.r2 = self.r2 + printable[1] + '    '
            self.r3 = self.r3 + '-' * printable[2] + '    '
            if len(printable) == 4:
                self.r4 = self.r4 + printable[3] + '    '

    def view(self):
        """ """
        print(self.r1)
        print(self.r2)
        print(self.r3)
        print(self.r4)


def ArithmeticArranger(strOperations, solve=False):
    """ Main working function """
    operations = [Operation(strOperation, solve).printable()
                  for strOperation in strOperations]

    viewer = Viewer(operations)
    viewer.view()


# ? Implementation
if __name__ == "__main__":
    ArithmeticArranger(
        ['1555 + 5', '2000 + 75', '8 - 444', '8 - 444'], True)
