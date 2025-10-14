def find_max(words):
    max_unique_char = 0
    max_word = ""
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > max_unique_char:
            max_unique_char = len(unique_chars)
            max_word = word
        elif len(unique_chars) == max_unique_char and word < max_word:
            max_word = word
    return max_word
