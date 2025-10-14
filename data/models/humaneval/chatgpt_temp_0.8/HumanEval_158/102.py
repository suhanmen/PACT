def find_max(words):
    unique_counts = []
    for word in words:
        unique_chars = set(word)
        unique_count = len(unique_chars)
        unique_counts.append((unique_count, word))
    max_count = max(unique_counts)[0]
    max_words = [word for count, word in unique_counts if count == max_count]
    return sorted(max_words)[0] if max_words else ""
