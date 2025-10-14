def select_words(s, n):
    if not s:
        return []
    vowels = set('aeiouAEIOU')
    result = []
    for word in s.split():
        consonants = len([ch for ch in word if ch not in vowels])
        if consonants == n:
            result.append(word)
    return result
