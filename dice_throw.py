"""
Gilberto Echeverria
Python 3.4.2

Simulator of a dice throw
"""

import random

ans = 'y'

while ans == 'y' or ans == 'Y':
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print("You got ", dice1, "and", dice2)
    if dice1 == dice2:
        print("You got a pair of ", dice1)

    ans = input("Another number? (yes: y / no: n) ")

"""
    # Validation that the user is entering correct values
    ans = 'a'

    while ans != 'y' and ans != 'Y' and ans != 'n' and ans != 'N':
        ans = input("Another number? (yes: y / no: n)")
        if ans != 'y' and ans != 'Y' and ans != 'n' and ans != 'N':
            print("That option is invalid. Use 'y' or 'n'")
"""
