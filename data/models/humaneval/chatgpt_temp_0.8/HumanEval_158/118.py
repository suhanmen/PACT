def find_max(words):
    max_unique_chars = 0
    max_words = []
    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            max_words = [word]
        elif unique_chars == max_unique_chars:
            max_words.append(word)
    
    if max_words:
        return sorted(max_words)[0]
    else:
        return ""
