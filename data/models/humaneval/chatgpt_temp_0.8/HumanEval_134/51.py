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
    txt = txt.strip() # Removes whitespace from beginning and end of string
    
    if len(txt) == 0: # If empty string, return False
        return False
    
    last_char = txt[-1] # Get last character of string
    
    if last_char.isalpha(): # If last character is alphabetical
        if " " not in txt: # If string has no spaces (i.e. only one word)
            return True
        elif " " in txt and last_char not in txt.split()[-1]: # If string has spaces and last character is not part of last word
            return True
    
    return False # If none of the above conditions are met, return False
