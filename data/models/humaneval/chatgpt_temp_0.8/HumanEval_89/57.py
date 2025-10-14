def encrypt(s):
    shift = 2 * 2 # rotate down by 4 places
    encrypted = ''
    for letter in s:
        if letter.isalpha():
            if letter.isupper():
                base = ord('A')
            else:
                base = ord('a')
            encrypted += chr((ord(letter) - base + shift) % 26 + base)
        else:
            encrypted += letter
    return encrypted
