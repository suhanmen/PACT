def check_if_last_char_is_a_letter(txt):
    if len(txt) > 0:
        if txt[-1].isalpha() and (len(txt.split()[-1]) == 1):
            return True
        else:
            return False
    else:
        return False
