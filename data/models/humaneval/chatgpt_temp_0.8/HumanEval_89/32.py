python
def encrypt(s):
    shift = 2 * 2
    encrypted = ""
    for letter in s:
        if letter.isalpha():
            if letter.isupper():
                encrypted += chr((ord(letter) - 65 + shift) % 26 + 65)
            else:
                encrypted += chr((ord(letter) - 97 + shift) % 26 + 97)
        else:
            encrypted += letter
    return encrypted
