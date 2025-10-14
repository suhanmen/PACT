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
    
    last_char = txt[-1]
    if not last_char.isalpha():
        return False
    
    words = txt.split()
    last_word = words[-1]
    if len(last_word) != len(txt) and last_word[-1] == last_char:
        return False
    
    return True
