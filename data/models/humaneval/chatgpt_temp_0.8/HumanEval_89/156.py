def encrypt(s):
    shift = 2*2  # shift down by two multiplied to two places
    result = ""
    for c in s:
        if c.isalpha():
            # shift the letter by the desired amount
            new_ascii = (ord(c) - ord('a') + shift) % 26 + ord('a')
            result += chr(new_ascii)
        else:
            result += c  # leave non-letters as they are
    return result
