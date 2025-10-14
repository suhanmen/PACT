def select_words(s, n):
    if not s:
        return []
    vowels = set("aeiouAEIOU")
    words = s.split()
    result = []
    for word in words:
        consonants = 0
        for letter in word:
            if letter not in vowels:
                consonants += 1
        if consonants == n:
            result.append(word)
    return result
