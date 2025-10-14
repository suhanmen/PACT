def find_max(words):
    max_unique = -1
    result = ""
    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique:
            max_unique = unique_chars
            result = word
        elif unique_chars == max_unique:
            result = min(result, word)
    return result
