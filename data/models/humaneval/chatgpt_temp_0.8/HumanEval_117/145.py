def select_words(s, n):
    # initialize an empty list to store the selected words
    selected_words = []
    
    # if the string is empty return an empty list
    if not s:
        return selected_words
    
    # split the string into words
    words = s.split()
    
    # initialize a set of consonants
    consonants = set("bcdfghjklmnpqrstvwxyz")
    
    # loop through each word in the list of words
    for word in words:
        # count the number of consonants in the word
        num_consonants = sum(letter in consonants for letter in word)
        # if the number of consonants is equal to n, add the word to the selected_words list
        if num_consonants == n:
            selected_words.append(word)
            
    # return the selected_words list
    return selected_words
