def find_max(words):
    max_word = ""
    max_count = 0
    for word in words:
        unique_chars = set(word)
        unique_count = len(unique_chars)
        if unique_count > max_count:
            max_word = word
            max_count = unique_count
        elif unique_count == max_count:
            max_word = min(max_word, word)
    return max_word
