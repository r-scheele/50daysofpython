
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
                
                err = position + shift_amount
                if alphabet[err] == 'v' or alphabet[err] == 'w' or alphabet[err] == 'x' or alphabet[err] == 'y' or alphabet[err] == 'z':
                    shift_amount = 1
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

