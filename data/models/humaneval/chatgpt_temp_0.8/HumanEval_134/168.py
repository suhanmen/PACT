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
    
    # Remove any trailing whitespaces
    txt = txt.rstrip()
    
    # Get the last character of the string
    last_char = txt[-1]
    
    # Check if the last character is a letter and not a part of a word
    if last_char.isalpha() and (len(txt.split()) == 1 or txt.split()[-1][-1] == last_char):
        return True
    else:
        return False
