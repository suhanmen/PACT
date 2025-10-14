def select_words(s, n):
    if not s: # if s is empty, return an empty list
        return []
    words = s.split() # split the string into words
    result = [] # initialize the list to be returned
    for word in words:
        consonants = 0 # initialize the count of consonants in the word
        for letter in word:
            if letter.lower() not in "aeiou" and letter.isalpha(): # check if letter is a consonant
                consonants += 1 # increment the count of consonants
        if consonants == n: # if the word has exactly n consonants, add it to the result list
            result.append(word)
    return result
