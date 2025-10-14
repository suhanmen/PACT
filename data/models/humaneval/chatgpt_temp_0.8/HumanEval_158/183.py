def find_max(words):
    max_word = ""
    max_unique = 0
    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique:
            max_word = word
            max_unique = unique_chars
        elif unique_chars == max_unique and word < max_word:
            max_word = word
            max_unique = unique_chars
    return max_word
