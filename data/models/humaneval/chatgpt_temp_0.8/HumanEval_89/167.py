def encrypt(s):
    result = ''
    for i in range(len(s)):
        char = s[i]
        if char.isupper():
            result += chr((ord(char) + (2*2)) % 26 + 65)
        else:
            result += chr((ord(char) + (2*2)) % 26 + 97)
    return result
