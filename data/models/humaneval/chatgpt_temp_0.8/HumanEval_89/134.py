def encrypt(s):
    rotated = ""
    for letter in s:
        # determine the ASCII code of the letter
        ascii_code = ord(letter)
        # shift the ASCII code down by 2 multiplied to two places
        rotated_ascii = ascii_code + 2**2
        # check if the rotated ASCII code is greater than the ASCII code for 'z'
        if rotated_ascii > ord('z'):
            # wrap around to the first letter 'a'
            rotated_ascii = rotated_ascii - 26
        # add the rotated letter to the encrypted string
        rotated += chr(rotated_ascii)
    return rotated
