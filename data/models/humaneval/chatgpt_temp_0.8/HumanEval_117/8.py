def select_words(s, n):
    if not s:
        return []
    words = s.split()
    result = []
    for word in words:
        consonants = sum(1 for c in word if c.isalpha() and c not in 'aeiouAEIOU')
        if consonants == n:
            result.append(word)
    return result
