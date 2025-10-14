def encrypt(s):
    shift = 2 * 2 # shift down by two multiplied to two places
    result = ''
    for c in s:
        if c.isalpha():
            # shift the character down by the shift amount,
            # taking into account the wraparound of the alphabet
            shifted = chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        else:
            shifted = c # leave non-alphabetic characters as is
        result += shifted
    return result
