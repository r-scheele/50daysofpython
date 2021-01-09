import time
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to BitUp Navigator.")
print("Your mission is to Enter the University of ilorin from my house.") 

lose = False
start = input("Enter start to begin your journey: ")
if 'start' or 'alright' or 'okay' or 'ok' in start:
    print('Lets begin shall we!')
    print('...')
    time.sleep(2)
    gate = input('Can you locate the gate? Yes or No: ').lower()
    door = True

    while door:
        if 'yes' or 'sure' or 'guess' in gate:
            door = False
            print('Please proceed')
            left_or_rigth = input('Proceed left or right: ')
            time.sleep(1)
            if 'right' in left_or_rigth:
                print('Walk on for a while')
                time.sleep(1)
                junction = input('You are now at a junctio. Do you want to move left or right? ')
                if 'left' in junction:
                    print('This is where you take a bike')
                    bike = input("Wanna take a bike? yes or No: ")
                    if 'yes' in bike:
                        print('cool')
                    else:
                        print('Issokay Na')
                else:
                    print('Still okay sha')
            else:
                print('Oops, you entered into a pit. Please try again')
                lose = True
                break
        else:
            print('Check well please')
else:
    print('You are on your own')

if lose:
    print('Game Over!!!')
