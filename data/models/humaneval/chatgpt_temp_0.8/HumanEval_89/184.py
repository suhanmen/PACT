def encrypt(s):
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    rotated_alphabet = ALPHABET[4:] + ALPHABET[:4]  # shift down by 2*2=4 places
    mapping = str.maketrans(ALPHABET, rotated_alphabet)
    return s.translate(mapping)
