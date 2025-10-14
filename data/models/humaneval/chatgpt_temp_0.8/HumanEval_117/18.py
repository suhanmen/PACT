def select_words(s, n):
    result = []
    if not s:
        return result
    words = s.split()
    for word in words:
        consonants = 0
        for letter in word:
            if letter not in "aeiouAEIOU":
                consonants += 1
        if consonants == n:
            result.append(word)
    return result
