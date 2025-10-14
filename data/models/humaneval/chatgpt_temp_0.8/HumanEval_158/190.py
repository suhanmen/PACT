def find_max(words):
    max_word = ""
    max_unique_chars = 0

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_word = word
            max_unique_chars = unique_chars
        elif unique_chars == max_unique_chars:
            max_word = min(max_word, word)

    return max_word
