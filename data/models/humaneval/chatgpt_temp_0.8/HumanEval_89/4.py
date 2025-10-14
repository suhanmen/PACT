def encrypt(s):
    shift = 2 * 2 # multiply by two to shift two places
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    encrypted_string = ""
    for char in s:
        if char.isalpha():
            if char.isupper():
                index = (shifted_alphabet.index(char.lower()) + shift) % 26
                encrypted_string += shifted_alphabet[index].upper()
            else:
                index = (shifted_alphabet.index(char) + shift) % 26
                encrypted_string += shifted_alphabet[index]
        else:
            encrypted_string += char
    return encrypted_string
