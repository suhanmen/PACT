def encrypt(s):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""
    for char in s:
        if char.isalpha():
            new_char = alphabets[(alphabets.index(char) + (2 * 2)) % 26]
            encrypted += new_char
        else:
            encrypted += char
    return encrypted
