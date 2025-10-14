def anti_shuffle(s):
    words = s.split()
    new_words = []
    for word in words:
        sorted_chars = "".join(sorted(word))
        new_words.append(sorted_chars)
    return " ".join(new_words)
