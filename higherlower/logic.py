import os
from art import logo,vs
from game_data import data
import random


def check_answer(guess, account_a, account_b):
    """Takes a guess input and checks if it matches the answer."""
    
    if  account_a['follower_count'] > account_b['follower_count']:
        return guess == 'A'
    else:
        return guess == 'B'

def format_account(account):
    name = account['name']
    desc = account['description']
    country = account['country']

    return f"{name}, A {desc} from {country}"


def game():
    game_on = True
    score = 0

    first_account = random.choice(data)
    second_account = random.choice(data)

    if first_account == second_account:
        second_account = random.choice(data)

    while game_on:

        print(logo)

        if score != 0:
            print(f"You're right. current score: {score}")

        print(format_account(first_account))
        print(vs)
        print(format_account(second_account))

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

       
        result = check_answer(guess, first_account, second_account)

        if result:
            score += 1

            first_account, second_account = second_account, random.choice(data)
            os.system('clear')
        else:
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            game_on = False


game()



