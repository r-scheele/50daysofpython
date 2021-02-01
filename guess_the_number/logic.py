import random
from art import logo


def game():
    print(logo)
    print("I'm thinking of a number between 1 to 100")
    correct_answer = random.randint(1, 100)

    difficulty = input("Choose a difficulty, Type 'hard' or 'easy': ")


    def compare(a, b):
        if a == b:
            global game_over
            game_over = True
            return f'You win, the correct answer is {correct_answer}'
        elif a > b:
            return 'Too high '
        elif a < b:
            return 'Too low '



    if difficulty == 'hard':
        guesses = 5
    elif difficulty == 'easy':
        guesses = 10

    game_over = False

    while not game_over:
        guess = int(input("Make a guess: "))
        print(compare(guess, correct_answer))
    
        guesses -= 1

        if guesses == 0:
            print("You've run out of guesses, you lose.")
            game_over = True
        else:
            print(f'Guess again \nYou have {guesses} attempts remaining to guess the number.')

        
         
        
        
end_game = False

while not end_game:
    if input("Do you want to play a guessing game? Type 'y' or 'n': ").lower() == 'y':
        game()
    else:
        end_game = True

