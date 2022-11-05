"""
STATUS: Working

OVERVIEW: This python file will extract all the emails present in the finding text file and store it in the log file

IMPROVEMENTS:
    - FIXME  Make it more dynamic
        => make it so, that it could be used for some other function such as finding phone no.
    - Improve the Regular Expression
    - TODO Document


"""

# @ Imports
from ntpath import join
import os
import re
from datetime import datetime


# * Defining

textFilePath = join(os.getcwd(), "Email Finder\\Finding Text")

with open(textFilePath, "r") as find:
    finding_string = find.read()

emailReEx = re.compile(r'[a-zA-Z]+[0-9]*(@[a-zA-Z]+\.(com|net))')

emails = emailReEx.finditer(finding_string)


def EnterEmail(email):
    """This function will store the email given to it in the file"""
    with open("log.txt", "a") as log:
        log.write("- " + email + "\n")


# ? Implementation
if __name__ == "__main__":
    with open("log.txt", "a") as log:
        log.write("\n")
        log.write(str(datetime.today()))
        log.write("\n")

    [EnterEmail(email.group()) for email in emails]
