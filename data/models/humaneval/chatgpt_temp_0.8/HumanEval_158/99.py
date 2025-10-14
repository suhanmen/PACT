def find_max(words):
    max_word = ""
    max_count = -1
    for word in words:
        unique_chars = set(word)
        count = len(unique_chars)
        if count > max_count:
            max_count = count
            max_word = word
        elif count == max_count:
            max_word = min(max_word, word)
    return max_word
