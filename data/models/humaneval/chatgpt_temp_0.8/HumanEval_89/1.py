def encrypt(s):
    encrypted = ''
    for letter in s:
        if letter.isalpha():
            new_letter = chr((ord(letter) - 97 + 2*2) % 26 + 97)
            encrypted += new_letter
        else:
            encrypted += letter
    return encrypted
