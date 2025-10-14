def encrypt(s):
    result = ""
    for letter in s:
        if letter.isalpha():
            shifted_letter = chr((ord(letter) - 97 + 2*2) % 26 + 97)
            result += shifted_letter
        else:
            result += letter
    return result
