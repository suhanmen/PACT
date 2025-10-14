def select_words(s, n):
    if not s:  # if the string is empty
        return []
    words = s.split()  # split the string into words
    result = []
    for word in words:
        consonants = 0
        for letter in word:
            if letter.isalpha() and letter.lower() not in "aeiou":  # check if the letter is a consonant
                consonants += 1
        if consonants == n:
            result.append(word)
    return result
