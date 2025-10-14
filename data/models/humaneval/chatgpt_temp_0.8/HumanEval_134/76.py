def check_if_last_char_is_a_letter(txt):
    if len(txt) == 0:
        return False
    elif not txt[-1].isalpha():
        return False
    else:
        words = txt.split()
        last_word = words[-1]
        if len(last_word) == 1:
            return True
        else:
            return not last_word[-2].isalpha()
