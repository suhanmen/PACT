def check_if_last_char_is_a_letter(txt):
    if len(txt) == 0 or not txt[-1].isalpha():
        return False
    words = txt.split(" ")
    last_word = words[-1]
    if len(last_word) == 1:
        return True
    else:
        return last_word[-1].isalpha() and not last_word[-2].isalpha()
