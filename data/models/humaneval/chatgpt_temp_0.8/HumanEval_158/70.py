def find_max(words):
    max_chars = 0
    max_word = ""
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > max_chars:
            max_chars = len(unique_chars)
            max_word = word
        elif len(unique_chars) == max_chars:
            if word < max_word:
                max_word = word
    return max_word
