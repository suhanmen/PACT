def select_words(s, n):
    # If the string is empty, return an empty list
    if not s:
        return []
    
    # Define a function to check if a letter is a consonant
    def is_consonant(c):
        return c.lower() not in "aeiou"
    
    # Split the string into a list of words
    words = s.split()
    
    # Initialize an empty list to store the words with n consonants
    result = []
    
    # Iterate through each word in the list
    for word in words:
        # Count the number of consonants in the word
        num_consonants = sum([1 for c in word if is_consonant(c)])
        # If the word has n consonants, append it to the result list
        if num_consonants == n:
            result.append(word)
    
    # Return the result list
    return result
