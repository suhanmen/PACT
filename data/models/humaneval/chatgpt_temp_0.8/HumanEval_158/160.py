def find_max(words):
    max_unique_chars = 0
    result = ''
    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            result = word
        elif unique_chars == max_unique_chars:
            result = min(result, word)
    return result
