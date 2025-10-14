def encrypt(s):
    """
    Create a function encrypt that takes a string as an argument and returns a
    string encrypted with the alphabet being rotated. The alphabet should be rotated
    in a manner such that the letters shift down by two multiplied to two places.
    """
    result = ""
    for char in s:
        if char.isalpha():
            # shift the character by two multiplied to two places
            shifted_char = chr((ord(char) - 97 + 2*2) % 26 + 97)
            result += shifted_char
        else:
            # ignore non-alphabetic characters
            result += char
    return result
