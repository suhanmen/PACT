def select_words(s, n):
    if not s:
        return []
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    words = s.split()
    selected_words = []
    for word in words:
        consonant_count = sum(1 for letter in word if letter in consonants)
        if consonant_count == n:
            selected_words.append(word)
    return selected_words
