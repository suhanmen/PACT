def find_max(words):
    unique_chars = {}
    for word in words:
        unique_chars[word] = len(set(word))
    max_chars = max(unique_chars.values())
    max_words = [word for word, count in unique_chars.items() if count == max_chars]
    return sorted(max_words)[0] if max_words else ""
