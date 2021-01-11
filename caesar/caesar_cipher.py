from arts import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def caesar(start_text, shift_amount, cipher_direction):

    if cipher_direction != 'decode' and cipher_direction != 'encode':
        return 'Invalid direction'
    #2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    text = ''
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == 'encode':
            text += alphabet[position + shift_amount]
        else:
            text += alphabet[position - shift_amount]
    return f"The {cipher_direction}d text is {text}"

    


print(caesar(text, shift, direction))