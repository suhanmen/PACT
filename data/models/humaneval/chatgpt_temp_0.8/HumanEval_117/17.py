def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    
    # create a list of consonants
    consonants = "bcdfghjklmnpqrstvwxyz"
    
    # split the string into words
    words = s.split()
    
    # initialize a list to store the result
    result = []
    
    # iterate over the words
    for word in words:
        
        # initialize a counter for consonants
        consonant_count = 0
        
        # iterate over the characters in the word
        for char in word:
            
            # if the character is a consonant, increment the counter
            if char.lower() in consonants:
                consonant_count += 1
                
        # if the word contains exactly n consonants, append it to the result
        if consonant_count == n:
            result.append(word)
            
    return result
