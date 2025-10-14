def check_if_last_char_is_a_letter(txt):
    if len(txt) == 0:
        return False
    # get the last character of the string and check if it is alphabetical
    last_char = txt[-1]
    if not last_char.isalpha():
        return False
    # check if the last character is not part of a word
    words = txt.split()
    last_word = words[-1]
    if last_char in last_word:
        return False
    return True
