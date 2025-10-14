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
    if not txt:
        return False

    # Get the last character of the string
    last_char = txt[-1]

    # If the last character is not alphabetical, return False
    if not last_char.isalpha():
        return False

    # If the last character is part of a word, return False
    if len(txt.split()[-1]) > 1:
        return False

    return True
