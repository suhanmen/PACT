def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[4:] + alphabet[:4]
    encrypted = ''
    for letter in s:
        if letter.isalpha():
            shifted_index = (shifted_alphabet.index(letter) + 2*2) % 26
            encrypted += shifted_alphabet[shifted_index]
        else:
            encrypted += letter
    return encrypted
