def select_words(s, n):
    if not s:  # empty string case
        return []
    words = s.split()  # split the string into words
    result = []
    for word in words:
        consonants = 0
        for letter in word:
            if letter.lower() not in "aeiou":  # count consonants
                consonants += 1
        if consonants == n:  # add word to result if it matches n
            result.append(word)
    return result
