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
    txt = txt.strip() # Remove any trailing spaces
    if not txt: # If txt is an empty string
        return False 
    last_char = txt[-1]
    if last_char.isalpha():
        # Check if the last character is not part of a word
        return len(txt.split()[-1]) == 1
    return False
