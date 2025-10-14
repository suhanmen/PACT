def anti_shuffle(s):
    # Split the string into words
    words = s.split()
    
    # Create an empty list to store the ordered words
    ordered_words = []
    
    # Loop through each word
    for word in words:
        # Convert the word into a list of characters
        chars = list(word)
        
        # Sort the characters in ascending order based on ascii value
        chars.sort()
        
        # Join the sorted characters back into a string
        ordered_word = ''.join(chars)
        
        # Add the ordered word to the list of ordered words
        ordered_words.append(ordered_word)
    
    # Combine the ordered words back into a string, preserving the original spaces
    ordered_string = ' '.join(ordered_words)
    
    return ordered_string
