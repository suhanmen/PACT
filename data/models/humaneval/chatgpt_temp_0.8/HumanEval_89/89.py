def encrypt(s):
    result = ''
    for letter in s:
        # Convert letter to its ASCII code
        letter_code = ord(letter)
        # Shift the letter code down by 2 multiplied to 2 places
        new_code = letter_code + (2*2)
        # Check if the new code is outside the alphabets range
        if new_code > ord('z'):
            new_code -= 26
        # Convert new code back to the corresponding letter
        new_letter = chr(new_code)
        # Add the new letter to the result
        result += new_letter
    return result
