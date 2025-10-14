def find_max(words):
    max_word = ""
    max_count = 0
    for word in words:
        unique_count = len(set(word))
        if unique_count > max_count:
            max_word = word
            max_count = unique_count
        elif unique_count == max_count:
            max_word = min(word, max_word)
    return max_word
