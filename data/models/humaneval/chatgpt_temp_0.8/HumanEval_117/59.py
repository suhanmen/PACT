def select_words(s, n):
    if not s:
        return []
    words = s.split()
    result = []
    for word in words:
        consonant_count = sum(1 for c in word if c not in 'aeiouAEIOU')
        if consonant_count == n:
            result.append(word)
    return result
