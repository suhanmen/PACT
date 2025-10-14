def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''

    # Get the last character in the string
    last_char = txt[-1]

    # Check if the last character is a letter and not a space
    if last_char.isalpha() and last_char != " ":
        # Check if the last word contains the last character
        if last_char in txt.split()[-1]:
            return False
        else:
            return True
    else:
        return False
