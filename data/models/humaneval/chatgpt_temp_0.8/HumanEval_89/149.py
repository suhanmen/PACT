def encrypt(s):
    new_s = ''
    for char in s:
        if char.isalpha():
            new_char = chr((ord(char) - 97 + (2 * 2)) % 26 + 97)
            new_s += new_char
        else:
            new_s += char
    return new_s
