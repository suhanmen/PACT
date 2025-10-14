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
    if not txt:  # if the string is empty
        return False

    # Get the last character and check if it is a letter
    last_char = txt[-1]
    if not last_char.isalpha():
        return False

    # Get the last word and check if the last character is part of a word
    last_word = txt.split()[-1]
    return last_char not in last_word
