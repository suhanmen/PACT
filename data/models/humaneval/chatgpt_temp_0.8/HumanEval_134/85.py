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
    # remove any trailing white space and split the string into words
    words = txt.strip().split()
    
    # get the last word
    last_word = words[-1] if words else ''
    
    # check if the last character of the last word is a letter
    if last_word and last_word[-1].isalpha():
        # check if the last word is a single character
        if len(last_word) == 1:
            return True
        else:
            # check if the second-last character of the last word is a space
            second_last_char = last_word[-2]
            if second_last_char.isspace():
                return True
    return False
