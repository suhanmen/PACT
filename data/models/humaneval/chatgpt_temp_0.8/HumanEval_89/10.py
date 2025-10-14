def encrypt(s):
    """
    Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    result = ""
    for letter in s:
        if letter.isalpha():
            # Shift the letter by two multiplied to two places
            new_letter_ascii = ord(letter) + (2 * 2)
            # If the new letter is outside of the range of a-z or A-Z, wrap around
            if letter.isupper() and new_letter_ascii > ord('Z') or \
                letter.islower() and new_letter_ascii > ord('z'):
                new_letter_ascii -= 26
            result += chr(new_letter_ascii)
        else:
            result += letter
    return result
