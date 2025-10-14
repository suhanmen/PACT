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
    if txt and not txt.isspace(): # check if txt is not empty or all whitespace
        words = txt.split() # split txt into words
        last_word = words[-1] # get the last word
        if len(last_word) == 1 and last_word.isalpha(): # check if last word is a single letter and is alphabetical
            return True
        elif len(last_word) > 1 and last_word[-1].isalpha() and not last_word[-2].isalpha(): # check if last character is alphabetical and not part of a word
            return True
    return False # return False if txt is empty or all whitespace, or if last character is not alphabetical or part of a word.
