def find_max(words):
    max_chars = -1
    max_word = ""
    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_chars or (unique_chars == max_chars and word < max_word):
            max_chars = unique_chars
            max_word = word
    return max_word
