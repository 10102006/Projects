"""
STATUS: Working

OVERVIEW: In this program we are going to find the factorial and the fibonacci squence of a given number then add them to find how many trailling zeros is has.

$ Can be improved work for future

"""

# * Defining

def Fac_Fib_Zeros(given_number):
    """
    What is to be done:
        1. Finding the factorial => 5*4*3*2*1
        2. Finding the fibonacci squence number => 1+1+2+3+5+8+13
        3. Adding them
        4. Finding the trailling zeros
            1. Making a list of the numbers
            2. Checking for continuous zeros
    """

    # @ Calculating the factorial
    factorial = 1
    for iteration in range(given_number):
        factorial*= (given_number - iteration)

    # @ Calculating the Fibonacci squence
    fibonacci = 0
    i = 1
    j = 1
    for _ in range(given_number):
        fibonacci = i+j
        i = j
        j = fibonacci

    # $ Calculating the trailing zeros
    end_number = str(factorial * fibonacci)

    trailing_zeros = 0

    for digit in end_number:
        if digit == "0":
            trailing_zeros+=1
        else:
            trailing_zeros = 0

    print(end_number)
    print(trailing_zeros)

# ? Implementation
if __name__ == "__main__":
   Fac_Fib_Zeros(25)