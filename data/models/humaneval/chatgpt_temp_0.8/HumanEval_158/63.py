def find_max(words):
    max_chars = 0
    result = ''
    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_chars:
            max_chars = unique_chars
            result = word
        elif unique_chars == max_chars and word < result:
            result = word
    return result
