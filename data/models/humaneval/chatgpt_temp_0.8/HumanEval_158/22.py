def find_max(words):
    max_word = ""
    max_count = 0
    for word in words:
        count = len(set(word))
        if count > max_count:
            max_count = count
            max_word = word
        elif count == max_count and word < max_word:
            max_word = word
    return max_word
