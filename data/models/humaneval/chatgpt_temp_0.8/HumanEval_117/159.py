def select_words(s, n):
    """
    Given a string s and a natural number n, returns a list of all words from string s that 
    contain exactly n consonants, in the order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    """
    if not s:
        return []
    
    # Define a helper function to check if a given string has exactly n consonants
    def has_n_consonants(word):
        consonants = "bcdfghjklmnpqrstvwxyz"
        n_consonants = 0
        for char in word:
            if char.lower() in consonants:
                n_consonants += 1
        return n_consonants == n
    
    # Split the input string into words
    words = s.split()
    
    # Filter the words based on the number of consonants they contain
    selected_words = [word for word in words if has_n_consonants(word)]
    
    return selected_words
