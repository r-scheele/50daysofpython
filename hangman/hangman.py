import random
import os
from hangman_words import word_list
from hangman_arts import stages, logo




print(logo)
#-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
#-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# guess = input('Guess a letter: ').lower()
#3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.


#4: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display.append('-')



#6: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
end_of_game = False
answer = ''
lives = 0

while not end_of_game:
    if '-' not in display:
        print('You win!!!')
        break

    #ALTERNATIVELY
    # if len(answer) == word_length - 1:
    #     end_of_game = True
    
    guess = input('Guess a letter: ').lower()
    
    os.system("clear")
    position = 0

    if guess in display:
        print(f"You've already guessed {guess}")
    
 #: - If guess is not a letter in the chosen_word,
#Then reduce 'lives' by 1. 
#If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(stages[lives])
        lives += 1

    if lives == 6:
        print(f"The correct is {chosen_word}")
        print('You lose!!!')
        break

#5: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    for letter in chosen_word:
        if letter == guess:
            display[position] = letter
            answer += letter
        else:
            pass
        position += 1
    
    
    print(f"{' '.join(display)}")