def find_max(words):
    max_uniq_chars = 0
    max_word = ""

    for word in words:
        uniq_chars = len(set(word))
        if uniq_chars > max_uniq_chars:
            max_uniq_chars = uniq_chars
            max_word = word
        elif uniq_chars == max_uniq_chars:
            if word < max_word:
                max_word = word

    return max_word
