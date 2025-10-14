def find_max(words):
    max_word = ""
    max_chars = 0

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_chars or (unique_chars == max_chars and word < max_word):
            max_word = word
            max_chars = unique_chars

    return max_word
