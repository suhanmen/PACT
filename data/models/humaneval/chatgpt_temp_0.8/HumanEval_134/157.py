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

    # Split the string into words
    words = txt.split()

    # Get the last word
    last_word = words[-1]

    # Check if the last character is a letter and is not a part of a word
    if last_word and not last_word[-1].isalpha():
        return False
    elif last_word and not last_word[:-1].isalpha():
        return True
    else:
        return False
