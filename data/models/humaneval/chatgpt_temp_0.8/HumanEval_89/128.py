def encrypt(s):
    shift = 2 * 2
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, rotated)
    return s.translate(table)
