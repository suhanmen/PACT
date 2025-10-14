def find_max(words):
    max_count = 0
    max_word = ""
    for word in words:
        count = len(set(word))
        if count > max_count:
            max_count = count
            max_word = word
        elif count == max_count:
            max_word = min(word, max_word)
    return max_word
