def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_alphabet = alphabet[4:] + alphabet[:4] # rotate alphabet down by 2*2 places
    table = str.maketrans(alphabet, new_alphabet)
    return s.translate(table)
