def encrypt(s):
    result = ""
    for char in s:
        if char.isalpha():
            index = ord(char.lower()) - 97
            index = (index + (2*2)) % 26
            result += chr(index + 97)
        else:
            result += char
    return result
