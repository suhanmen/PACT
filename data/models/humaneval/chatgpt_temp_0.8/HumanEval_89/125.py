python
def encrypt(s):
    result = ""
    for c in s:
        if c.isalpha():
            offset = (ord(c) - ord('a') + 2*2) % 26  # calculate the new letter position
            result += chr(ord('a') + offset)  # add the new letter to the result string
        else:
            result += c  # add non-letter characters as they are
    return result
