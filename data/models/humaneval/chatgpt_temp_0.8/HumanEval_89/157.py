def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted = alphabet[2 * 2:] + alphabet[:2 * 2]
    mapping = str.maketrans(alphabet, shifted)
    return s.translate(mapping)
