def find_max(words):
    max_unique_count = 0
    max_unique_word = ''
    for word in words:
        unique_count = len(set(word))
        if unique_count > max_unique_count:
            max_unique_count = unique_count
            max_unique_word = word
        elif unique_count == max_unique_count and word < max_unique_word:
            max_unique_word = word
    return max_unique_word
