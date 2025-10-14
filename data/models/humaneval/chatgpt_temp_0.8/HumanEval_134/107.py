def check_if_last_char_is_a_letter(txt):
    if txt.strip() == "":
        return False
    last_char = txt.strip()[-1]
    if not last_char.isalpha():
        return False
    if " " in txt.strip()[:-1]:
        if last_char not in txt.strip()[:-1].split()[-1]:
            return True
        else:
            return False
    else:
        return True
