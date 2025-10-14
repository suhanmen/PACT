def find_max(words):
    word_dict = {}
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) not in word_dict:
            word_dict[len(unique_chars)] = []
        word_dict[len(unique_chars)].append(word)
    max_unique_chars = max(word_dict.keys())
    return sorted(word_dict[max_unique_chars])[0]
