def find_max(words):
    max_word = ""
    max_count = 0
    for word in words:
        unique_chars = set(word)
        count_unique_chars = len(unique_chars)
        if count_unique_chars > max_count:
            max_word = word
            max_count = count_unique_chars
        elif count_unique_chars == max_count:
            if word < max_word:
                max_word = word
    return max_word
