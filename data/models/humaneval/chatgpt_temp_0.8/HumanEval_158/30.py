def find_max(words):
    unique_chars = 0
    max_word = ""

    for word in words:
        count = len(set(word))
        if count > unique_chars:
            unique_chars = count
            max_word = word
        elif count == unique_chars and word < max_word:
            max_word = word

    return max_word
