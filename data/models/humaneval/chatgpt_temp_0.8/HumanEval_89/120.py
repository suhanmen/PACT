def encrypt(s):
    new_str = ""
    for char in s:
        if char.isalpha():
            new_char = chr((ord(char) - 97 + (2*2)) % 26 + 97)
            new_str += new_char
        else:
            new_str += char
    return new_str
