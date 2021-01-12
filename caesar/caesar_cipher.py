from arts import logo
from logic import caesar

print(logo)




should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 25:
        shift = shift % 25
    if shift % 25 == 0:
        shift = shift + 4
    caesar(text, shift, direction)

    response = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if response == 'no' or response == 'n':
        should_continue = False
        print('Goodbye')


        