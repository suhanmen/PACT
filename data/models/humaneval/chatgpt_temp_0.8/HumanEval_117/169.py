def select_words(s, n):
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    result = []
    for word in s.split():
        num_consonants = sum(1 for c in word if c in consonants)
        if num_consonants == n:
            result.append(word)
    return result
