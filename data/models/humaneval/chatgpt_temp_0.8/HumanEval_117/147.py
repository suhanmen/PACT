def select_words(s, n):
    result = []
    if not s:
        return result
    for word in s.split():
        consonants = 0
        for c in word:
            if c.lower() not in "aeiou" and c.isalpha():
                consonants += 1
        if consonants == n:
            result.append(word)
    return result
