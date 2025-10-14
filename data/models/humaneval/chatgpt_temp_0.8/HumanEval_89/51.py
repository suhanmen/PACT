def encrypt(s):
    shift = 2 * 2  # shift down by two multiplied to two places
    result = ""
    for c in s:
        if c.isalpha():
            new_val = (ord(c.lower()) - 97 + shift) % 26 + 97
            result += chr(new_val)
        else:
            result += c
    return result
