def find_max(words):
    max_num_unique_chars = 0
    max_word = ""

    for word in words:
        num_unique_chars = len(set(word))
        if num_unique_chars > max_num_unique_chars:
            max_num_unique_chars = num_unique_chars
            max_word = word
        elif num_unique_chars == max_num_unique_chars:
            max_word = min(max_word, word)

    return max_word
