def find_max(words):
    max_unique = 0
    result = ""
    for word in words:
        unique_chars = set(word)
        num_unique = len(unique_chars)
        if num_unique > max_unique:
            max_unique = num_unique
            result = word
        elif num_unique == max_unique:
            result = min(result, word)
    return result
