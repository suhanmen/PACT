def select_words(s, n):
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    words = s.split()
    result = []
    for word in words:
        consonant_count = sum(1 for letter in word if letter in consonants)
        if consonant_count == n:
            result.append(word)
    return result
