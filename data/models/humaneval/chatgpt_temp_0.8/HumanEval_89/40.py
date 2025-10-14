def encrypt(s):
    shift = 2 * 2
    result = ""
    for c in s:
        if c.isalpha():
            if c.islower():
                result += chr((ord(c) - 97 + shift) % 26 + 97)
            else:
                result += chr((ord(c) - 65 + shift) % 26 + 65)
        else:
            result += c
    return result
