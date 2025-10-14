def check_if_last_char_is_a_letter(txt):
    if len(txt) == 0:
        return False
    elif not txt[-1].isalpha():
        return False
    elif txt[-1] in txt[:-1]:
        return False
    else:
        return True
