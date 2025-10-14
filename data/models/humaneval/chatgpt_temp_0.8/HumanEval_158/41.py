def find_max(words):
    max_word = ""
    max_count = 0
    for word in words:
        count = len(set(word))
        if count > max_count:
            max_word = word
            max_count = count
        elif count == max_count:
            max_word = min(max_word, word)
    return max_word
