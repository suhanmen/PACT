def find_max(words):
    max_chars = 0
    max_word = ""

    for word in words:
        unique_chars = set(word)
        num_unique_chars = len(unique_chars)

        if num_unique_chars > max_chars:
            max_chars = num_unique_chars
            max_word = word
        elif num_unique_chars == max_chars and word < max_word:
            max_word = word

    return max_word
