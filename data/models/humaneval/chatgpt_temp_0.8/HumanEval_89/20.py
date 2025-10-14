def encrypt(s):
    shift = 2*2
    encrypted = ""
    for letter in s:
        if letter.isalpha():
            shifted_letter = chr((ord(letter) - 97 + shift) % 26 + 97)
            encrypted += shifted_letter
        else:
            encrypted += letter
    return encrypted
