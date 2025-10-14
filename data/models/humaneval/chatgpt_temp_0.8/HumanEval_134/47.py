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
        return False # if string is empty, return False
    
    last_char = txt[-1] # get last character of string
    if not last_char.isalpha():
        return False # if last character is not an alphabetical character, return False
    
    words = txt.split() # split string into words
    last_word = words[-1] # get last word in string
    if last_char in last_word:
        return False # if last character is part of a word, return False
    
    return True # if last character is not part of a word and is alphabetical, return True
