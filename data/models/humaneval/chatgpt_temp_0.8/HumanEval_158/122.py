def find_max(words):
    max_unique_count = 0
    max_unique_word = ""

    for word in words:
        unique_chars = set(word)
        num_unique_chars = len(unique_chars)

        if num_unique_chars > max_unique_count:
            max_unique_count = num_unique_chars
            max_unique_word = word
        elif num_unique_chars == max_unique_count:
            if word < max_unique_word:
                max_unique_word = word

    return max_unique_word
