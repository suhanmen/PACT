def check_if_last_char_is_a_letter(txt):
    if len(txt) == 0:
        return False
    last_char = txt[-1]
    if last_char.isalpha() and (len(txt) == 1 or txt[-2] == ' ') and last_char != ' ':
        return True
    else:
        return False
