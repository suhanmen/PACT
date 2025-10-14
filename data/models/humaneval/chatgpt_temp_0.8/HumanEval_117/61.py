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
    # Create a list to store words with n consonants
    words = []
    
    # Split the string into words
    s = s.split()
    
    # Iterate over each word in the string
    for word in s:
        
        # Count the number of consonants in the word
        consonants = 0
        for letter in word:
            if letter.lower() not in 'aeiou':
                consonants += 1
        
        # If the word has n consonants, append it to the list
        if consonants == n:
            words.append(word)
    
    # Return the list of words with n consonants
    return words
