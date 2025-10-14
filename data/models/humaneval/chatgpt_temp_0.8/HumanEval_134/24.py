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

    # Split the input string by space to get a list of words
    words = txt.split()

    # If the input string has only one word, check if its last character is an alphabetical character
    if len(words) == 1:
        last_char = words[0][-1]
        return last_char.isalpha() and not (words[0][:-1].isalpha())

    # If the input string has more than one word, check if the last character of the last word is an alphabetical character
    else:
        last_char = words[-1][-1]
        return last_char.isalpha() and not (words[-1][:-1].isalpha())
