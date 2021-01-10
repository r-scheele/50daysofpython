import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input('What do you choose? type 0 for Rock, 1 for Paper or 2 for Scissors\n'))

computer_choice = random.randint(0, 1)
game_images = [rock, paper, scissors]
print(game_images[user_choice])

print('Computer chose: '+ str(computer_choice))
print(game_images[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print('You win')
elif user_choice < 0 or user_choice >= 3:
    print('You typed in an invalid number')
elif computer_choice == 0 and user_choice == 2:
    print('You lose')
elif computer_choice > user_choice:
    print('You lose')
elif computer_choice < user_choice:
    print('You lose')
elif computer_choice == user_choice:
    print('Draw')


