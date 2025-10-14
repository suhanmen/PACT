def select_words(s, n):
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    words = s.split()
    results = []
    for word in words:
        count_consonants = 0
        for letter in word:
            if letter in consonants:
                count_consonants += 1
        if count_consonants == n:
            results.append(word)
    return results
