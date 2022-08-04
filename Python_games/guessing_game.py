import random
from sys import _enablelegacywindowsfsencoding


def guess():
    number_player_chose = x
    number_computer_generated = 0
    guess = random.randint(1, 101)
    while True:
        answer = input("pick a number from 1-100")
        result = number_computer_generated
        if (answer == result):
            print("You chose correctly")
        elif answer > guess:
            for x in range(guess):
                if x < guess:
                    print ("You were off by " + str(number_computer_generated) + "numbers")
        elif answer > guess:
            print ("You were off by " + str(number_computer_generated) + "numbers")