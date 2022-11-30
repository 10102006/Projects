"""
STATUS: Working

OVERVIEW: Basic board functionalities

IMPROVEMENTS:
    - TODO printing can be improved
    - TODO optimise speed

"""

# @ Imports
import numpy


# * Defining

class Board:
    '''
    Handles all the board related stuff
    '''

    def __init__(self, rows=3, columns=3):
        """
        initiating rows, columns and empty-board
        """
        self.numberOfRows = rows
        self.numberOfColumns = columns
        self.MakeBoard()

    def MakeBoard(self): self.board = numpy.array(
        [[' ' for _ in range(self.numberOfColumns)] for _ in range(self.numberOfRows)])

    def IndexedBoard(self): self.board = numpy.array([numpy.arange(
        (self.numberOfColumns*i)+1, (self.numberOfColumns * (i+1))+1) for i in range(self.numberOfRows)])

    def PrintBoard(self):
        '''
        prints the board in a visual format
        '''
        for i, row in enumerate(self.board):
            [print(ele) if i == self.numberOfColumns-1
             else print(ele, end=' | ') for i, ele in enumerate(row)]
            [print() if i == self.numberOfRows -
             1 else print('-' * self.numberOfColumns*3)]

    def ChangeCell(self, obj, coordinate=tuple):
        """
        change cel of matrix
        """
        self.board[coordinate[0]][coordinate[1]] = obj

    def GetCoordinates(self, cellIndex):
        """
        find coord using indexes calculations
        """
        cellIndex -= 1
        row, col = cellIndex//3, cellIndex % 3
        return (row, col)


# ? Implementation
if __name__ == "__main__":
    bd = Board()
