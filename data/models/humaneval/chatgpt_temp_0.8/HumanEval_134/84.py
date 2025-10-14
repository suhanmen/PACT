def check_if_last_char_is_a_letter(txt):
    if len(txt) == 0:
        return False
    elif not txt[-1].isalpha():
        return False
    elif txt[-1] == " ":
        return False
    elif " " in txt[:-1]:
        if txt[:-1].split(" ")[-1][-1].isalpha():
            return False
        else:
            return True
    else:
        return True
