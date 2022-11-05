"""
STATUS: Working

OVERVIEW: Simplified Calculator

IMPROVEMENTS:
    - Add tons of features
    - like discounting
    - Key points for purchase
    - history of purchase
    -TODO Just make this shit into something showable

This will be contained in a true where the price of the items will be added on as the new price is add and if q or enter is pressed the program will quit showing the end amount

"""


# * Defining

def Receipt_Generator():
    amount = 0

    index = 1
    while True:
        new_Price = input(f"Enter the item no. {index} price: ")
        if new_Price.isnumeric():
            index += 1
            amount += int(new_Price)
        elif new_Price == "q":
            break
        else:
            print("*** Wrong input! ***")

    print('-----------------------------------------')
    print("Total amount is : ", amount)


# ? Implementation
if __name__ == "__main__":
    Receipt_Generator()
