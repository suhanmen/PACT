def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[4:] + alphabet[:4]
    shifted_alphabet += shifted_alphabet
    encrypted = ''
    for letter in s:
        if letter in alphabet:
            index = alphabet.index(letter)
            encrypted += shifted_alphabet[index]
        else:
            encrypted += letter
    return encrypted
