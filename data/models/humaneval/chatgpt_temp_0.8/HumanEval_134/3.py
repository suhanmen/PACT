python
def check_if_last_char_is_a_letter(txt):
    if not txt:
        return False # returns False for empty strings
    words = txt.split()
    last_word = words[-1] if words else '' # gets last word if exists
    if len(last_word) == 1 and last_word.isalpha():
        return True # returns True if last character is a single alphabetical character
    if last_word[-1].isalpha() and last_word[-2] == " ":
        return True # returns True if last character is an alphabetical character and is not a part of a word
    return False # returns False for all other cases
