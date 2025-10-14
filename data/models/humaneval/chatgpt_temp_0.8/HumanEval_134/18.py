def check_if_last_char_is_a_letter(txt):
    if len(txt) < 1:
        return False
    elif not txt[-1].isalpha():
        return False
    else:
        txt = txt.strip()
        if " " in txt:
            last_word = txt.split()[-1]
            if len(last_word) == 1:
                return True
            else:
                return False
        else:
            return True
