def select_words(s, n):
    if not s:
        return []
    words = s.split()
    res = []
    for word in words:
        consonants = sum(1 for c in word if c.isalpha() and c not in "aeiouAEIOU")
        if consonants == n:
            res.append(word)
    return res
