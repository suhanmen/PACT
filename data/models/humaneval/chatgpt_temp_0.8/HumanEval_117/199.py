def select_words(s, n):
    if not s: # if the string is empty
        return [] # return empty list
    words = s.split() # split string into words
    result = [] # initialize result list
    for word in words: # loop through each word
        consonants = 0 # initialize consonants count
        for letter in word: # loop through each letter in the word
            if letter not in "aeiouAEIOU" and letter.isalpha(): # check if it's a consonant
                consonants += 1 # increment consonants count
        if consonants == n: # if word contains exactly n consonants
            result.append(word) # add it to result list
    return result # return result list
