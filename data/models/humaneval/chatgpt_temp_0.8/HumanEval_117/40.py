def select_words(s, n):
    if not s: # if s is empty
        return [] # return an empty list
    words = s.split() # split the string into words
    result = [] # initialize an empty list to store the selected words
    for word in words:
        consonants = sum(1 for c in word if c.lower() not in 'aeiou') # count the number of consonants in the word
        if consonants == n: # if the word contains exactly n consonants
            result.append(word) # append the word to the result list
    return result # return the result list
