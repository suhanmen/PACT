def find_max(words):
    max_word = ""
    max_num = 0
    for word in words:
        unique_chars = set(word)
        num_unique_chars = len(unique_chars)
        if num_unique_chars > max_num:
            max_num = num_unique_chars
            max_word = word
        elif num_unique_chars == max_num and word < max_word:
            max_word = word
    return max_word
