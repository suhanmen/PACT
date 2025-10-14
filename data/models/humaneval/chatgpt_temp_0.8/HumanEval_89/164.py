def encrypt(s):
    shift = 2 * 2  # calculate the shift value
    result = ""  # initialize an empty string to hold the encrypted string
    for char in s:  # for each character in the input string
        if char.isalpha():  # if the character is a letter
            new_char = chr((ord(char) - 97 + shift) % 26 + 97)  # rotate the letter and convert back to character
            result += new_char  # add the rotated letter to the result string
        else:  # if the character is not a letter, add it to the result string as-is
            result += char
    return result
