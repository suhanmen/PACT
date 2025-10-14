def check_if_last_char_is_a_letter(txt):
    if txt == "":
        return False

    # Split the string into words
    words = txt.split()

    # Check if the last word exists and the last character of the last word is a letter
    if len(words) > 0 and words[-1][-1].isalpha() and words[-1][-1] not in words[-1][:-1]:
        return True
    else:
        return False
