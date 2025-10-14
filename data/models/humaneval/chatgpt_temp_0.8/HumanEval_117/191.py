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
    
    # Define a list of consonants
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    
    # Split the string into words
    words = s.split()
    
    # Initialize an empty list to hold the selected words
    selected_words = []
    
    # Iterate over each word
    for word in words:
        
        # Initialize a counter for the number of consonants in the word
        consonant_count = 0
        
        # Iterate over each character in the word
        for char in word:
            
            # If the character is a consonant, increment the consonant count
            if char.lower() in consonants:
                consonant_count += 1
                
        # If the consonant count matches the desired number of consonants, add the word to the selected words list
        if consonant_count == n:
            selected_words.append(word)
            
    # Return the list of selected words
    return
