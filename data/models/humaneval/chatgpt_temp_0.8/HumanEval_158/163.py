python
def find_max(words):
    max_unique_chars = 0
    max_word = ""
    for word in sorted(words):
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            max_word = word
    return max_word
