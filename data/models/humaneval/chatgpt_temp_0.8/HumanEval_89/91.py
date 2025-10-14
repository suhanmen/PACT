def encrypt(s):
    shifted_alphabet = ''
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        shifted_letter = chr((ord(letter) - 97 + 2*2) % 26 + 97)
        shifted_alphabet += shifted_letter
    encrypted_string = ''
    for letter in s:
        if letter.isalpha():
            if letter.isupper():
                encrypted_string += shifted_alphabet[ord(letter.lower()) - 97].upper()
            else:
                encrypted_string += shifted_alphabet[ord(letter) - 97]
        else:
            encrypted_string += letter
    return encrypted_string
