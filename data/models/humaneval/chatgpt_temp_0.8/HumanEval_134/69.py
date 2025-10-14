def check_if_last_char_is_a_letter(txt):
    if not txt:
        return False
    last_char = txt[-1]
    if last_char.isalpha() and (len(txt) == 1 or txt[-2] == " ") and (len(txt) == txt.count(" ")+1):
        return True
    else:
        return False
