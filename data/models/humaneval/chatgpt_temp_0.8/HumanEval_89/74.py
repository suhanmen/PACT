def encrypt(s):
    shift = 2 * 2
    encrypted = ''
    for char in s.lower():
        if char.isalpha():
            new_char = chr((ord(char) - 97 + shift) % 26 + 97)
            encrypted += new_char
        else:
            encrypted += char
    return encrypted
