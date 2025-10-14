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
    if len(txt) == 0:
        return False

    # Split the string into words
    words = txt.split()

    # Get the last word
    last_word = words[-1]

    # Check if the last character of the last word is an alphabetical character and 
    # is not part of a word
    if last_word.isalpha() and len(last_word) == 1:
        return True
    else:
        return False
