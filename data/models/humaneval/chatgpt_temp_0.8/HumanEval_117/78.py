def select_words(s, n):
    if s == "":
        return []
    words = s.split()
    result = []
    for w in words:
        consonants = 0
        for c in w:
            if c.lower() not in "aeiou":
                consonants += 1
        if consonants == n:
            result.append(w)
    return result
