def select_words(s, n):
    if not s: # if s is empty
        return []
    words = s.split() # split s into words
    result = []
    for word in words:
        consonants = 0
        for letter in word:
            if letter.lower() not in "aeiou" and letter.isalpha():
                consonants += 1
        if consonants == n:
            result.append(word)
    return result
