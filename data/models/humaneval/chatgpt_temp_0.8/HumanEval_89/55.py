def encrypt(s):
    shift = 2 * 2
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_alphabet = alphabet[shift:] + alphabet[:shift]
    return s.translate(str.maketrans(alphabet, new_alphabet))
