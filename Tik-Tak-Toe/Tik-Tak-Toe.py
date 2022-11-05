'''
STATUS: Not Working

OVERVIEW: Was a good tic-tac-toe game

IMPROVEMENTS:
    - TODO readthrough

'''


# * Imports
import random

# @ Defination


def MakeBoard(withIndex=False, n_row=3, n_column=3):
    """
    What is done:
        1. Making a temporary list as the main-board list
        2. With rowIndex as the multiplicant we can change the index numbers
        3. Appending a list three times in the main list:
            1. This list will contain the indexes if the indexes is required which is acquired by multiplicant rowIndex
            2. If the indexing is not required then the space will be empty
        4. Increasing the rowIndex each itration so that the gap between each row will be of the number of rows
        5. Returning the main-board list
    """
    # ? Main-board list
    t_list = []

    # * rowIndex will help in indexing between the rows
    rowIndex = 1

    # @ Since we need three rows the iteration will loop three times
    for _ in range(n_row):

        # @ This will make a list if the indexing is required else we will continue with the empty cells
        cells = [
            f'{index + rowIndex}' if withIndex else ' ' for index in range(n_column)]

        # ? Appending the above formed list
        t_list.append(cells)
        rowIndex += n_column

    # ? Returing the list
    return t_list


def PrintBoard(boardObj=MakeBoard()):
    """
    What is done:
        1. We are looping the 2D list
        2. Using so decorators we are beautifing the content
        3. We are ending empty so that the row will be same line
        4. Thus we are doing an empty print to break the line
    """

    for boxRow in boardObj:
        print('\t', end=' ')
        for value in boxRow:
            print(f'[{value}]', end=' ')
        print('')


def ChangeCell(boardObj, rowindex=0, columnindex=0, turn=' ', coordinate=()):
    """
    What is done:
        1. The rowindex and columnindex can used seperately if need we just need to decrease the value by 1 to get the correct numeration
        2. Other than the above method we can still use the coordinates to directly give the coordinate through the get coordinates method
        3. The coordinates are seperated to the rowindex and columnindex for simplicity
        4. The cell value is the removed value as we will add value there
        5. As a precation we will not remove the value is a value is already present
            ** We are not remove but we are re-adding the value obtained through the pop
        6. If the cell is empty then we will be add the turn value which can be either
            ** {'X'} or {'O'}
        7. For further precaution we will be returning an bool to cofirm the status of cell change if the cell is not changed then the turn must not be taken
    """
    # ? Modificing the rowindex and columnindex to be compatable
    rowindex = int(coordinate[0] if coordinate else rowindex) - 1
    columnindex = int(coordinate[1] if coordinate else columnindex) - 1

    # ? Obtaining and removing the cell which is to be change
    cellvalue = boardObj[rowindex].pop(columnindex)

    # * If the cell had some value in it then it must be corrected
    if cellvalue != ' ':
        boardObj[rowindex].insert(columnindex, cellvalue)
        return False
    # * Otherwise we can change the cell according to the turn
    else:
        boardObj[rowindex].insert(columnindex, turn)
        return True


def GetCoordinates(cellIndex):
    """
    What is done:
        1. Making and indexed board using the MakeBoard() method => This will return a board which has index values in it which represents its coordinates
        2. Looping through the 2D board:
            1. Storing the indexes of both row and the column number
            2. If the cell value of the indexed board matches the index asked then the coordinates will be returned
            3. Returning the tuple coordinates
    """
    # ? Reference indexed board
    indexedBoard = MakeBoard(True)

    # * This is a 2D loop Which is looping through the Indexed-Board
    for rowIndex, boxRow in enumerate(indexedBoard):
        for columnIndex, value in enumerate(boxRow):
            # * Checking if the values of the cell (index) if equal to the asked index
            if value == str(cellIndex):
                return (rowIndex + 1, columnIndex + 1)


def Won(boardObj):
    """
    What is done:
        1. Making a function to check if the cell values of certain index's of cell were equal => See the function for further understanding
        2. Generating the possible winning states
            ** These will contain the config of index which can be said to be a victory
        3. Looping through all the winning configaration if and config is true then we will return true
        4. But if the loop has ended and there if no config available then we will return false
    """

    def CheckWin(winstate):
        """
        What is done:
            1. Finding and storing the coordinates of all the indexed given in the config
            2. Using the coordinates to find the values in the cells
            3. Checking if the cell as not empty
            4. If they are empty then returing false else contiuing
            5. Checking if the cell values are equal using the euler axiom
            6. If all the condition are met then returing true
        """
        # ? Storing the coordinate tuple using the GetCoordinates() method
        coord1 = GetCoordinates(winstate[0])
        coord2 = GetCoordinates(winstate[1])
        coord3 = GetCoordinates(winstate[2])

        # @ Using tuple splicing obtaing the rowindex and columnindex of the cell
        cell1 = boardObj[coord1[0] - 1][coord1[1] - 1]
        cell2 = boardObj[coord2[0] - 1][coord2[1] - 1]
        cell3 = boardObj[coord3[0] - 1][coord3[1] - 1]

        # * Checking logic
        if cell1 != ' ':
            if cell1 == cell2 and cell2 == cell3:
                return True

        return False

    # $ Make this autogenerated for more configaration
    winStates = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7)
    ]

    # ? Looping through all the winstate checking if any config works
    for winstate in winStates:
        if CheckWin(winstate):
            return True

    # ? Returing false if the conditions are not met
    return False


def OneGame(boardObj):
    """
    What is done:
        1. First Randomnly generating a random turn
        2. Printing the for reference of player & Using a seperator to cleanup
        3. turnIndex help with error handling of the number of turns
        4. Semi-game Loop:
            1. Checking if there is any win condition then breaking the loop
            2. Printing whose turn it is
            3. Print the board conditions using the PrintBoard() method
            4. Finding the coordinates of the cell which the player has selected using GetCoordinates()
            5. Changing the cell state using the ChangeCell() method and turn
            6. Turn Check
                1. Using the bool returned by the ChangeCell() we are checking if any cell is selected or not if not then not changing the turn or increasing the turn
                2. Else we will be Switch the turn
                3. Seperator for cleanup because there will be lot of reiteration
            7. Printing the end result because the end board is omitted
            8. Again checking the status of completed board if it is a won then return the name of player won
            9. But it was because turn exhaution then we will be calling it a draw
    """
    # @ Random turn incounter
    turn = ['X', 'O'][random.randint(0, 1)]

    # ? Printing the indexed board for reference
    PrintBoard(MakeBoard(withIndex=True))

    print('----------------------------------------------------------------------')

    # ? Turn index for number of turn related problems
    turnIndex = 1

    # * We would break the loop if the turn number is 9 => Meaning all the cells are filled
    while turnIndex <= 9:

        # * Checking if any win condition is met => Break out of the loop
        if Won(boardObj):
            break

        # ? Printing whoose turn it is for convienince
        print(f"{turn}'s Turn")

        # * This is for refernce of current board state
        PrintBoard(boardObj)

        # @ This is the asking mechanism and getting the coordinates of the asked cell
        coordinates = GetCoordinates(int(input('Enter the Cell Index: ')))

        # * Filling the cell which is asked with the currt turn
        cellTaken = ChangeCell(
            boardObj=boardObj, coordinate=coordinates, turn=turn)

        # * Checking if any cell is taken or not
        if cellTaken:
            # * This will increase the turn if cell is taken
            turnIndex = turnIndex + 1

            # @ We are also switch the turn
            turn = SwitchTurn(turn)

        # * Otherwise we will not change the turn of increase the turnindex
        else:
            turnIndex = turnIndex

        print('----------------------------------------------------------------------')

    # ? This is the final state of the board
    PrintBoard(boardObj)

    # * We are checking if the board state is won or draw
    if Won(boardObj):
        # ? If won the print the name of player who won then return the value for score stuff
        print(f'\t *** {SwitchTurn(turn)} Won! ***')
        return SwitchTurn(turn)
    else:
        # ? Else nothing will happen just we will print draw
        print('\t *** Draw ***')
        return 'draw'


def FullGame(score=[0, 0]):
    """
    What is done: 
        1. We wil running this loop forever meaning we can play the game as much as we want 
        2. Main loop:
            1. Playing a game using the OneGame() method
            2. And storing the winners name
            3. If the winner is X then Adding 1 to the score[0] => score of x is collected in this index else we will be adding to the o index
            4. Score stuff:
                1. Removing and Retrieving the score of the player
                2. Add 1 to the the var and then appending that to the score with appropriate index
            5. Asking for the player if they want to continue using the input break => this is a special forever loop breaker
            6. Print the score if they want to continue another game
        3. Printing the score as the end result
    """
    while True:
        winner = OneGame(MakeBoard())
        if winner == 'X':
            currentscore = score.pop(0)
        else:
            currentscore = score.pop(1)

        finalscore = currentscore + 1
        score.insert(0 if winner == 'X' else 1, finalscore)

        if input('Do you want to continue(Y/N): ').capitalize() == 'N':
            print(f'*** Score- X : {score[0]} / O : {score[1]} ***')
            break

        print('----------------------------------------------------------------------')
        print(f'Score- X : {score[0]} / O : {score[1]}')
        print('----------------------------------------------------------------------')
    print(f'Score- X : {score[0]} / O : {score[1]}')


def GenerateWinStates(n_rows=3, n_columns=3):
    """
    """
    # ? Main-board list
    winstates = []

    # horizontal wins
    # row_index = 1
    # for _ in range(n_rows):
    #     winstate = []
    #     for _ in range(n_columns):
    #         winstate = [index + row_index for index in range(n_columns)]
    #     winstates.append(winstate)
    #     row_index += n_columns

    # vertical wins
    # column_index = 1
    # for _ in range(n_columns):
    #     winstate = []
    #     for row in range(n_rows):
    #         winstate.append(column_index + (n_rows * row))
    #     winstates.append(winstate)
    #     column_index += 1

    # diagonal wins
    # column_index = 1
    # for _ in range(n_columns - (n_rows - 1)):
    #     indexes = [index + 1 for index in range(n_rows * n_columns)]
    #     winstate = []
    #     for row in range(n_rows):
    #         index = column_index + ((n_rows + n_columns - 2) * row)
    #         winstate.append(index if index in indexes else '')
    #     column_index += 1
    #     winstates.append(winstate)

    return winstates

# ? Implementation


# * This will required to change the turn of the player
def SwitchTurn(turn): return 'X' if turn == 'O' else 'O'


if __name__ == "__main__":
    # board = MakeBoard()
    # ChangeCell(board, 1, 1, 'x')
    # ChangeCell(board, 2, 2, 'o')
    # ChangeCell(board, 3, 3, 'x')

    # PrintBoard(board)

    # coord = GetCoordinates(1)

    # print(Won(board))

    FullGame()
