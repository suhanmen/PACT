def find_max(words):
    max_word = ""
    max_count = 0
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > max_count:
            max_word = word
            max_count = len(unique_chars)
        elif len(unique_chars) == max_count:
            if word < max_word:
                max_word = word
    return max_word
