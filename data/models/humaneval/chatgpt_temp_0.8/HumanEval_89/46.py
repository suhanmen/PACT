def encrypt(s):
    rotated = ''.join([chr((ord(c) - 97 + 2 * 2) % 26 + 97) if c.isalpha() else c for c in s])
    return rotated
