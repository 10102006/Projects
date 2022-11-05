'''
STATUS: Working

OVERVIEW: Simple typying practice code with some logging in(not checked)

IMPROVEMENTS:
    - TODO readthrough

Things done:
      1. MakeRandomText(numberofletters, firstletter, lastletter, caps):
            1. numberofletter is self explanatory
            2. the letter will be assigned from the first and last letter var
            3. caps will randomly make some text capitalize
            4. This will also sometimes make the space inside the string
      2. UserInput(rf_string):
            1. Take input from the user
            2. Check how good the user had done and store the marks in a hash table
            3. Returning the hash table for score generation
      3. CalculateScore(hs_score, time):
            1. hs_score will be the hash_table returned from the above method
            2. First we will append the score of the hash table in a list
            3. Then we will do some calculation for the score generation calculation in detail is done bellow
            4. then we will return the score
      4. LogRunTime(str_time, end_time) =>
            1. str_time and end_time are the timing which I had sperately stored in the __main__, I will pass this to the function for it make a log
            2. We first making the main log file which will contain a string as the base then there will the current month name
            3. I will be making the file appending at the last this will contain nothing much

'''


# * Imports
import random
from datetime import datetime
import time

total_score = []

# @ Defining


def MakeRandomText(numberofletters, caps=False):
    """
        1. This will first Import random for using it
        2. We will iterate till the number of letter are met
        3. Each time we will append this character to a list
        4. Then we will join this list as a string and then intialise it
        5. lastly we will return this string made
    """
    letter_sequence = []

    for _ in range(numberofletters):
        # * Generating a random character
        char = chr(random.randint(ord('a'), ord('z')))

    # ! This will randomly make a chacter capitalised if caps is on
        if caps:
            # * This will randomly chose a number
            t_caps = random.randint(0, 2)

            # $ If the number is 0 then the letter will be capitalise else it will be small
            char = char.capitalize() if t_caps == 0 else char

    # @ This will generate spaces inside the string but it will be rare
        t_space = random.randint(0, 3)
        char = '' if t_space == 0 else char
        letter_sequence.append(char)

 # * Joining letter_squence to make it into a string
    f_sequence = ''.join(letter_sequence)
    return f_sequence


def UserInput(reference_string):
    """
        1. Taking input then storing that
        2. Making a list for both the string for easy formatting
        3. Making a hash table for storing the results
        4. looping Through all the input_list then checking if the index is correct or not
        5. If the input is correct then marking it as true else it will remain false
        6. The intialise all this to the hash-table
        7. returning the hashtable
    """
    typing_input = input(reference_string + '\n')

 # * This will sperate the strings to make them into a list
    l_reference_string = [_str for _str in reference_string]
    l_input = [_str for _str in typing_input]

 # * This is a hash table for telling how many correct words have been typed
    hs_input = dict.fromkeys(l_reference_string)

 # @ This is the checking method
    # ? We will first loop through the l_input with an index
    for i, rf_str in enumerate(l_input):
        # $ We are making a hash table for storing how many charcter we got correct
        # ? So in that hash table we will make the value of the letter to be true if it is correct else it will be false
        if rf_str == l_reference_string[i]:
            hs_input[rf_str] = True
        else:
            hs_input[rf_str] = False

    # * Returning the hash-table so that the calculate can analise it
    return hs_input


def CalculateScore(hs_score, time):
    """
        1. Making a list with short-hand
            1. Looping thorough the hash-table and getting the values
            2. If the value is True then intialising 1 else 0
        2. Finding the score:
            1. Dividing the base number(10) with the length for one item score
            2. Multiply the item score with the number of 1 in the list
            3. The subtracting the total with time cost
            4. Time cost is determined by the time taken / length so more time with more items will be equal
        3. returning the score
    """
    # $ Making a list with the hash-table given as arg
    # * This hash table contains true or false values for each letter
    # * So we are intialising a 1 if it is true else we are intialising 0
    l_score = [1 if value else 0 for value in hs_score.values()]

    # $ This is main calculation working
    f_score = int(
        (
            # * We are multiplying the lenght of l_score beacause this will give us a 2-digit number as a score
            # $ We are using the one value method to calculate the score which is find the value of one then multiply it by number of values
            (100 / len(l_score)) * l_score.count(1)

            # * We are also decreasing the total value by the time taken by the length of score
            # $ We are dividing the time with length to get a constant for each length
        ) - (time / len(l_score))
    )

    # * We are appending this score to the f_score for initalising the average score to the log
    total_score.append(f_score)
    return f_score


def LogTheRunTime(str_time, end_time):
    """
        1. Import os for directory functions
        2. First we have to change the directory for the make the log file in specific place
        3. Naming the filename as TyprLog_current - current/month so there will be a log of each month seperately
        4. Trying to open the logfile with w for making the file
        5. Then in the end it will add the info to the file like the date and the practice time
        6. I am also calculating the average score of the user in the current practice time
    """
    import os

  # @ Saving the path to the database and Changing the dir
    logdir = os.path.join(os.getcwd(), '/Logs')
    os.chdir(logdir)

  # ? Here Calculating the average score
    avg_score = 0
    # * Adding each score to the avg_score
    for score in total_score:
        avg_score += score
    # * Using the average method we are calculating the avg_score
    avg_score = avg_score / len(total_score)

  # @ Intialising the name of the
    logFileName = f'TyPrLog_{datetime.now().month}.txt'

    try:
        # @ Intialising the log file
        with open(logFileName, "w") as logbook:
            pass
    finally:
        with open(logFileName, "a") as logbook:
            # ? This is for Writing the basic template
            logbook.write(
                f'\nDate {datetime.now().date()}\n\t {str_time} -- {end_time} \n')
            logbook.write(f'\t Average Score: {avg_score}\n')
            logbook.write(
                '-------------------------------------------------------------------------------- \n')


def TypingPractice(no_letter, caps):
    """
        1. Intialising random text with text var
        2. Enter input for user to get ready
        3. Using time module to intialise the time after bellow final time
        4. Running the LetterChecker function to get the user input and storing the return hash table
        5. Subtracting the time to get the run
        6. Print the score with the calculateScore method.
    """

    # @ Making random text using
    r_text = (MakeRandomText(no_letter, caps))

    # ? Dummy continue
    input('Press enter to countinue: ')

  # ? Here we Getting the time taken to input the text
    # @ Here we are storing intilial time
    initialtime = time.time()

    hash_t = UserInput(r_text)

    finaltime = time.time()
    timeTaken = finaltime - initialtime

    print('Your score is : ', CalculateScore(hash_t, timeTaken))
    print('----------------------------------------')


def ContinueLoop(inputContinue=1):
    """
        1. This is a template that I have copied for easily running the functions
        2. We are Loop indefinately
        3. Taking an input and turning that into bool value with short hand if-else
        4. Checking for the input and doing the function
        5. If we chose not to continue the loop will break
    """
    while True:
        input_tocontinue = True if int(
            input(f'{inputContinue} to continue 0 to end: ')) == inputContinue else False
        if input_tocontinue:

            # ! Paste the code you want to run here
            TypingPractice(no_letter, caps)
        else:
            break


# ? Execution
if __name__ == '__main__':
    str_time = datetime.now().time()

    no_letter = int(input('How many letter do you want: '))
    caps = True if int(input(
        'Do you want cap letters 1 for yes, 0 for no: ')) == 1 else False

    TypingPractice(no_letter, caps)
    ContinueLoop()

    end_time = datetime.now().time()
    LogTheRunTime(str_time, end_time)
