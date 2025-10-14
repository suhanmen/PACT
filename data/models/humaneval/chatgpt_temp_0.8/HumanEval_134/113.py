def check_if_last_char_is_a_letter(txt):
    if len(txt) == 0:
        return False
    else:
        last_char = txt[-1]
        if last_char.isalpha():
            last_word = txt.split()[-1]
            if last_char not in last_word:
                return True
    return False
