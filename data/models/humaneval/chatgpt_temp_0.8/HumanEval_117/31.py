def select_words(s, n):
    if not s: # if string is empty
        return []
    words = s.split() # split the string into words
    result = [] # to store the words with exactly n consonants
    for word in words:
        consonants = 0 # to count the number of consonants
        for letter in word:
            if letter.lower() not in "aeiou": # if letter is a consonant
                consonants += 1
        if consonants == n: # if the word has exactly n consonants
            result.append(word)
    return result
