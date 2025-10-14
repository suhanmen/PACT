def select_words(s, n):
    # Initialize an empty list to store the selected words
    selected_words = []
    
    # If the string is empty, return an empty list
    if not s:
        return selected_words
    
    # Split the string into words
    words = s.split()
    
    # Iterate through each word
    for word in words:
        # Count the number of consonants in the word
        consonant_count = sum(1 for letter in word.lower() if letter not in "aeiou")
        
        # If the consonant count matches the given n, add the word to the selected words list
        if consonant_count == n:
            selected_words.append(word)
    
    # Return the selected words list
    return selected_words
