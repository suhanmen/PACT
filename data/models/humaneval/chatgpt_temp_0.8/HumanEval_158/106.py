def find_max(words):
    max_chars = -1
    max_word = ''
    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_chars:
            max_chars = unique_chars
            max_word = word
        elif unique_chars == max_chars:
            max_word = min(max_word, word)
    return max_word
