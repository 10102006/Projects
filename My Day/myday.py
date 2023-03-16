"""
STATUS:
OVERVIEW:
IMPROVEMENTS:
Workings:
"""

# @ Imports
import argparse
from main import MyDay, Add, Change

# * Defining

PARSER = argparse.ArgumentParser(
    description='Helpful tool for scheduling and managing ones day.')

PARSER.add_argument('command', type=str,
                    help='available commands: show, add, change', choices=['show', 'add', 'change'])
PARSER.add_argument('-data', '-d', type=str,
                    help='available input: habit and KA', choices=['habit', 'key anchor'])
PARSER.add_argument('-multiple', '-m', action='store_true')

args = PARSER.parse_args()

# ? Implementation
if __name__ == "__main__":
    main = MyDay()

    if args.command == 'show':
        main.show()
        quit()

    try:
        func = Add if args.command == 'add' else Change
        if args.data == 'habit':
            func.event()
        elif args.data == 'key anchor':
            func.keyAnchor()
        else:
            raise Exception(
                'INCOMPLETE PROMPT: enter data to alter using (-d)')

        main.save()
    except Exception as e:
        print(e)
