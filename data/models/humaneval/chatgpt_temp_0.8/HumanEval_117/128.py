def select_words(s, n):
    if not s:
        return []
    result = []
    words = s.split()
    for word in words:
        consonants = [c for c in word if c not in "aeiouAEIOU"]
        if len(consonants) == n:
            result.append(word)
    return result
