def select_words(s, n):
    if len(s) == 0:
        return []
    result = []
    for word in s.split():
        consonants = 0
        for letter in word:
            if letter.lower() not in ['a', 'e', 'i', 'o', 'u'] and letter.isalpha():
                consonants += 1
        if consonants == n:
            result.append(word)
    return result
