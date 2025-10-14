def select_words(s, n):
    if not s:  # empty string case
        return []
    words = s.split()  # split string into words
    result = []
    for word in words:
        consonants = 0
        for char in word:
            if char.isalpha() and char.lower() not in "aeiou":
                consonants += 1
        if consonants == n:
            result.append(word)
    return result
