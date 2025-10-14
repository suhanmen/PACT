python
def check_if_last_char_is_a_letter(txt):
    if not txt:
        return False
    # Split the string by space to get individual words
    words = txt.split()
    # Get the last word
    last_word = words[-1]
    # Check if the last character of the last word is a letter
    if last_word.isalpha() and txt[-1] == last_word[-1]:
        return True
    else:
        return False
