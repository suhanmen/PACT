def check_if_last_char_is_a_letter(txt):
    if not txt:
        return False
    txt = txt.strip()
    last_char = txt[-1]
    if not last_char.isalpha():
        return False
    word_list = txt.split()
    last_word = word_list[-1]
    if len(last_word) == 1:
        return True
    else:
        return False
