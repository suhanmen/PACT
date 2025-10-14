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

    if len(txt) == 0:  # if the string is empty, return False
        return False

    last_char = txt[-1]  # get the last character of the string

    # if the last character is not alphabetical or is part of a word, return False
    if not last_char.isalpha() or last_char in txt.split()[-1]:
        return False

    # otherwise, return True
    return True
