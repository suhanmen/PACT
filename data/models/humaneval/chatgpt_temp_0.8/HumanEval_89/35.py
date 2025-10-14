def encrypt(s):
    import string
    alphabet = string.ascii_lowercase
    n = len(alphabet)
    shifted_alphabet = alphabet[-2*n:] + alphabet[:-2*n] # Rotate alphabet down by 2 * 2 places
    table = str.maketrans(alphabet, shifted_alphabet)
    return s.translate(table)
