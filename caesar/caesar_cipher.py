from arts import logo

print(logo)

alphabet = ['1','2','3','4','5','6','7','8','9','0','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def caesar(start_text, shift_amount, cipher_direction):

    if cipher_direction != 'decode' and cipher_direction != 'encode':
        return 'Invalid direction'
    #2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    text = ''
    for char in start_text:
        try:
            if char in alphabet:
                
                position = alphabet.index(char)
                if cipher_direction == 'encode':
                    if char == 'v' or char == 'w' or char == 'v' or char == 'x' or char == 'y' or char == 'z':
                        text += char
                    else:
                        text += alphabet[position + shift_amount]
                else:
                    if char == 'v' or char == 'w' or char == 'v' or char == 'x' or char == 'y' or char == 'z':
                        text += char
                    else:
                        text += alphabet[position - shift_amount]
            else:
                text += char
        except IndexError:
            text += char
            
    return print(f"Here's the {cipher_direction}d result: {text}")


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


        