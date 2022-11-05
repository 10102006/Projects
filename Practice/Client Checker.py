'''
STATUS: Somewhat Working

OVERVIEW: Something like a item storage

IMPROVEMENTS:
    - Make it into a client scheduler
    - TODO Readthrough

'''


# Clients name

# Clients Info
client1 = ['client1_Diet', 'client1_Exercise']
client2 = ['client2_Diet', 'client2_Exercise']
client3 = ['client3_Diet', 'client3_Exercise']

# Clients list
Clients = [client1, client2, client3]

# Optional
# Name = input('Press enter name to continue: ').capitalize()
# Clients.append(Name)

# Name2 = input('Press enter next name to continue: ').capitalize()
# Clients.append(Name2)

# Name3 = input('Press enter next name to continue: ').capitalize()
# Clients.append(Name3)
# Optional


# Given


def ReturnWithTimeStamp(WhatToLog):
    import datetime
    return f'{WhatToLog} at {datetime.datetime.now()}\n'


def MoreEfficient(WhatToDo):
    """
    This a function which I think is more efficient than the previus method 
    the previous method took 100 lines of code mostly repeats
    """
    if WhatToDo == 1:

        print('** Writing accessed **')
        clientNumber = int(input('Please enter your client number:\n'))

        if clientNumber < len(Clients) or clientNumber > len(Clients):

            clientFileNumber = int(
                input('Input the client file number: 1 for Diet and 2 for Exercise:\n'))

            clientFileName = ''

            if clientFileNumber == 1:
                clientFileName = f'client{clientNumber}_Diet.txt'
            elif clientFileNumber == 2:
                clientFileName = f'client{clientNumber}_Exercise.txt'
            else:
                print('Sorry wrong input!')

            value = input('Enter What you want to store:\n ')

            with open(clientFileName, 'a') as clientFile:
                clientFile.write(ReturnWithTimeStamp(value))

    if WhatToDo == 2:

        print('** Reading accessed **')
        clientNumber = int(input('Please enter your client number: \n'))

        if clientNumber < len(Clients) or clientNumber > len(Clients):

            clientFileNumber = int(
                input('Input the client file number: 1 for Diet and 2 for Exercise:\n'))

            clientFileName = ''

            if clientFileNumber == 1:
                clientFileName = f'client{clientNumber}_Diet.txt'
            elif clientFileNumber == 2:
                clientFileName = f'client{clientNumber}_Exercise.txt'
            else:
                print('Sorry wrong input!')
            with open(clientFileName) as clientFile:
                print(clientFile.read())

    else:
        print('Sorry Wrong input')
        pass


def MakeTheFiles():

    for index, file in enumerate(Clients):
        with open(file[0], 'w') as f:
            pass
        with open(file[1], 'w') as f2:
            pass
    print('Files made!')


def Main_Loop():

    restart = False

    while True:
        restart = True

        print('')
        while restart != False:
            functionWork = int(input(
                'If you want to write in the files press 1\nIf you want to Read the files press 0\n'))
            if functionWork == 1 or functionWork == 2:
                MoreEfficient(functionWork)
            else:
                print('Sorry wrong input!')
                break

        Continue = int(input('To Continue press 1 and To Exit press 0\n'))
        if Continue == 0:
            restart = False
            break


def FileCheck():
    ShouldBuildFiles = input(
        "Do you want to make the files: Y / N\n").capitalize()

    if ShouldBuildFiles == 'Y':
        MakeTheFiles()
    elif ShouldBuildFiles == 'N':
        pass
    else:
        print('Sorry Wrong Input!')


# ********************************************************

FileCheck()
Main_Loop()

# ********************************************************
