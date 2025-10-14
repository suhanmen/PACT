def check_if_last_char_is_a_letter(txt):
    if not txt:
        return False
    last_char = txt[-1]
    if last_char.isalpha() and (len(txt.split()) == 1 or not txt.split()[-1].isalpha()):
        return True
    return False
