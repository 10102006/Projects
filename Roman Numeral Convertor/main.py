# DOCUMENT.
"""
STATUS: Working

OVERVIEW: Inefficient but function roman converter

IMPROVEMENTS:
    - make a class
"""

# @ Imports

romanChart = {
    1000: "M",
    500: "D",
    100: "C",
    50: "L",
    10: "X",
    5: 'V',
    1: 'I'
}

# * Defining


def breakNumber(num):
    """
    # IMPROVE.
    """
    num = str(num)
    nums = []
    i = len(num) - 1
    for char in num:
        nums.append(int(char) * 10 ** i)
        i -= 1

    return nums


def checkDifference(num):
    """
    # TODO.
    """
    for int in romanChart.keys():
        for mul in [100, 10, 1]:
            difference = (int - mul)
            if difference == num:
                return (mul, int)
    return None


def getQuotient(num):
    quos = []
    for int, char in romanChart.items():
        quo, num = divmod(num, int)
        if quo:
            quos.append((quo, char))
    return quos


def convert(number):
    """
    break the numbers
    find if the difference is equal
    then check the remainder and quotient
    """
    if not (0 < int(number) <= 1000):
        raise

    roman = ''
    nums = breakNumber(number)
    for digit in nums:
        val = checkDifference(digit)
        if val:
            roman += f'{romanChart[val[0]]}{romanChart[val[1]]}'
        else:
            quos = getQuotient(digit)
            for quo in quos:
                roman += f'{quo[0] * quo[1]}'

    return roman


# ? Implementation
if __name__ == "__main__":
    r = convert(int(input()))
    print(r)
