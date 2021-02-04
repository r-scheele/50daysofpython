import os
from art import logo,vs
from helpers import test, compare






def game():
    game_on = True
    score = 0

    first = compare()
    second = compare()

    while game_on:

        print(logo)


        if score != 0:
            print(f"You're right. current score: {score}")

        print(f"Compare A: {first['name']}, {first['description']}")


        print(vs)
        print(f"Against B: {second['name']}, {second['description']}")

        ans = input("Who has more followers? Type 'A' or 'B': ").upper()

        l = {
            'A': first,
            'B': second
        }
        result = test(ans, first, second)

        if ans == result:
            score += 1

            first, second = l[result], compare()
            os.system('clear')
        else:
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            game_on = False


game()



