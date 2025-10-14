def select_words(s, n):
    vowel = set("aeiouAEIOU")
    result = []
    for word in s.split():
        consonants = 0
        for letter in word:
            if letter not in vowel:
                consonants += 1
        if consonants == n:
            result.append(word)
    return result
