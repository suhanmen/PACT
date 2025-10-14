def select_words(s, n):
    if not s: # check if s is empty, return empty list if true
        return []
    
    # define a list of consonants
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    
    # split the input string into a list of words
    words = s.split(' ')
    
    # initialize an empty list to store words with n consonants
    result = []
    
    # iterate over the words in the input string
    for word in words:
        count = 0  # initialize a counter for number of consonants in the word
        for letter in word:
            if letter.lower() in consonants:
                count += 1
        if count == n:  # append the word to the result list if it has n consonants
            result.append(word)
    
    return result
