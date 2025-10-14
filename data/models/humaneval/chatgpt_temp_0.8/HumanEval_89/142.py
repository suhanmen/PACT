def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_alphabet = alphabet[8:] + alphabet[:8] + alphabet[24:] + alphabet[16:24]
    encrypted = ''
    for letter in s:
        index = alphabet.index(letter)
        encrypted += new_alphabet[index]
    return encrypted
