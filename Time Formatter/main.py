"""
STATUS: Working
OVERVIEW:
IMPROVEMENTS:
Workings:
"""

# @ Imports
import time

# * Defining

def format_duration(second):
    if second <= 0:
        return 'now'

    def second_converter():
        seconds = second
        minutes = seconds//60
        hours = minutes//60
        days = hours//24
        years = days//365
        obj = (seconds%60, minutes%60, hours%24, days%365, years)
        return obj

    tm = second_converter()
    st = ['seconds', 'minutes', 'hours', 'days', 'years']
    fn = []

    for t, s in zip(tm, st):
        if t != 0:
            fn.append(f'{t} {s[:-1] if t == 1 else s}')

    fn.reverse()
    rt =(', '.join(fn[:-1]))

    if len(fn) > 1:
        rt += f' and {fn[-1]}'
    else:
        rt = fn[-1]

    return rt

# ? Implementation
if __name__ == "__main__":
   print(format_duration(15731080))
