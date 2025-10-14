def find_max(words):
    max_unique = 0
    max_word = ""
    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique:
            max_unique = unique_chars
            max_word = word
        elif unique_chars == max_unique and word < max_word:
            max_word = word
    return max_word
