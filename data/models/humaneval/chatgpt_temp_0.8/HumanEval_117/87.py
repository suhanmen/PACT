def select_words(s, n):
    if not s:
        return []
    words = s.split()
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    result = []
    for word in words:
        count = sum(1 for letter in word if letter in consonants)
        if count == n:
            result.append(word)
    return result
