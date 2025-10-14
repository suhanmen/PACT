def encrypt(s):
    result = ""
    shift = 2 * 2  # shift down by 4 places
    for c in s:
        if c.isalpha():
            if c.isupper():
                result += chr((ord(c) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(c) - 97 + shift) % 26 + 97)
        else:
            result += c
    return result
