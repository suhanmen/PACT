def find_max(words):
    max_unique_count = -1
    max_unique_word = ""
    for word in words:
        unique_chars = set(word)
        unique_count = len(unique_chars)
        if unique_count > max_unique_count:
            max_unique_count = unique_count
            max_unique_word = word
        elif unique_count == max_unique_count:
            max_unique_word = min(max_unique_word, word) # lexicographical comparison
    return max_unique_word
