def find_max(words):
    max_unique = 0
    max_word = ""
    for word in words:
        unique = len(set(word))
        if unique > max_unique or (unique == max_unique and word < max_word):
            max_unique = unique
            max_word = word
    return max_word
