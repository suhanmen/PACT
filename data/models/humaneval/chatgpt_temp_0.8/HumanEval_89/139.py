def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[4:] + alphabet[:4] # shift down by two multiplied to 2 places
    table = str.maketrans(alphabet, shifted_alphabet)
    return s.translate(table)
