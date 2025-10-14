def check_if_last_char_is_a_letter(txt):
    if txt == "":
        return False
    last_char = txt[-1]
    if not last_char.isalpha():
        return False
    if len(txt.split()[-1]) > 1:
        return False
    return True
