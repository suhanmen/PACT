python
def encrypt(s):
    shift = 2 * 2
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_alphabet = alphabet[shift:] + alphabet[:shift]
    encrypted = ''
    for letter in s:
        if letter in alphabet:
            index = alphabet.index(letter)
            encrypted += rotated_alphabet[index]
        else:
            encrypted += letter
    return encrypted
