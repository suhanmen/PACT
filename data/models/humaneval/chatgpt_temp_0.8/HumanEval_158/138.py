def find_max(words):
    max_unique_count = 0
    max_unique_word = ""
    for word in words:
        unique_chars = set(word)
        unique_chars_count = len(unique_chars)
        if unique_chars_count > max_unique_count:
            max_unique_count = unique_chars_count
            max_unique_word = word
        elif unique_chars_count == max_unique_count and word < max_unique_word:
            max_unique_word = word
    return max_unique_word
