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

    # Check if the input string is empty
    if not txt:
        return False

    # Split the string into words and get the last word
    words = txt.split()
    last_word = words[-1] if words else ''

    # Check if the last character of the last word is a letter
    if last_word and last_word[-1].isalpha():

        # If the last word has only one character, return True
        if len(last_word) == 1:
            return True

        # If the last character of the last word is not preceded by a space, return True
        elif last_word[-2] != ' ':
            return True

    # Return False otherwise
    return False
