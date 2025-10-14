def check_if_last_char_is_a_letter(txt):
    if len(txt) > 0 and txt[-1].isalpha() and (not txt[-2].isalpha() or txt[-2] == " "):
        return True
    else:
        return False
