def find_max(words):
    max_unique = 0
    max_word = ""
    for word in words:
        unique = len(set(word))
        if unique > max_unique:
            max_unique = unique
            max_word = word
        elif unique == max_unique:
            max_word = min(max_word, word)
    return max_word
