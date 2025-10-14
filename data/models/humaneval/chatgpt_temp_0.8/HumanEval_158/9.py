def find_max(words):
    max_count = 0
    max_word = ""
    for word in words:
        unique_chars = set(word)
        count_unique_chars = len(unique_chars)
        if count_unique_chars > max_count:
            max_count = count_unique_chars
            max_word = word
        elif count_unique_chars == max_count:
            max_word = min(max_word, word)
    return max_word
