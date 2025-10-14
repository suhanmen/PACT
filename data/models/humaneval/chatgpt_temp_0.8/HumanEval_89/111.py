def encrypt(s):
    shifted_alphabet = ""
    for c in "abcdefghijklmnopqrstuvwxyz":
        shifted_alphabet += chr((ord(c) - ord('a') + 2 * 2) % 26 + ord('a'))
    encrypted = ""
    for c in s:
        if c.isalpha():
            if c.isupper():
                encrypted += shifted_alphabet[ord(c.lower()) - ord('a')].upper()
            else:
                encrypted += shifted_alphabet[ord(c) - ord('a')]
        else:
            encrypted += c
    return encrypted
