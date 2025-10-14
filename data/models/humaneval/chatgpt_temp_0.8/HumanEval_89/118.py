def encrypt(s):
    shifted_alphabet = ''.join([chr((ord(c) - 97 + 2 * 2) % 26 + 97) for c in 'abcdefghijklmnopqrstuvwxyz'])
    return ''.join([shifted_alphabet[ord(c) - 97] for c in s])
