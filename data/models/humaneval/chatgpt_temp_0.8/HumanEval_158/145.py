def find_max(words):
    max_word = ""
    max_count = 0
    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_count:
            max_count = unique_chars
            max_word = word
        elif unique_chars == max_count:
            max_word = min(max_word, word)
    return max_word
