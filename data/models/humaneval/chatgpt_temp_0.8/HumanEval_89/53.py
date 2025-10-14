def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    result = ''
    for char in s:
        if char.isalpha():
            # find the index of the current character in the alphabet
            index = ord(char.lower()) - 97
            # shift the index down by 2 * 2 places
            new_index = (index + 8) % 26
            # determine the new character and add it to the result string
            new_char = chr(new_index + 97)
            if char.isupper():
                new_char = new_char.upper()
            result += new_char
        else:
            result += char
    return result
