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

    # Check if the string is empty
    if not txt:
        return False

    # Split the string into words and get the last word
    words = txt.split()
    last_word = words[-1] if words else ''

    # Check if the last character of the last word is a letter
    if last_word and last_word[-1].isalpha():
        # Check if the last word is not part of a bigger word
        if len(last_word) == 1 or not last_word[-2].isalpha():
            return True

    return False
