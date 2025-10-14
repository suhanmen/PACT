def check_if_last_char_is_a_letter(txt):
    if not txt:  # if the string is empty
        return False
    if txt[-1].isalpha():  # if the last character is alphabetical
        if len(txt.split()[-1]) == 1:  # if the last character is not part of a word
            return True
    return False
