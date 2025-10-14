def check_if_last_char_is_a_letter(txt):
    if not txt:
        return False
    txt = txt.strip()
    if txt[-1].isalpha() and txt[-2] == " ":
        return True
    return False
