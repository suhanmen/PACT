def find_max(words):
    max_count = 0
    max_word = ""
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > max_count:
            max_count = len(unique_chars)
            max_word = word
        elif len(unique_chars) == max_count:
            max_word = min(max_word, word)
    return max_word
