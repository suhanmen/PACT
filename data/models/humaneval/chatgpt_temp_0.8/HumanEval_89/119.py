def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[2:] + alphabet[:2]  # shift alphabet down by 2*2 = 4
    table = str.maketrans(alphabet, shifted_alphabet)
    return s.translate(table)
