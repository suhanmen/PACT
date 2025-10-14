def find_max(words):
    max_word = ""
    max_unique = 0
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > max_unique:
            max_word = word
            max_unique = len(unique_chars)
        elif len(unique_chars) == max_unique:
            if word < max_word:
                max_word = word
    return max_word
