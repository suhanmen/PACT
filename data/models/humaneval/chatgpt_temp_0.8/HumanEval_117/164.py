def select_words(s, n):
    if not s:
        return []
    words = s.split()
    res = []
    for w in words:
        consonants = [c for c in w if c not in "aeiouAEIOU"]
        if len(consonants) == n:
            res.append(w)
    return res
