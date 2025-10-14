def anti_shuffle(s):
    # Split the input string into a list of words
    words = s.split()
    
    # Create an empty list to store the ordered words
    ordered_words = []
    
    # Loop through each word in the list of words
    for word in words:
        # Convert the word to a list of characters and sort them by ascii value
        ordered_chars = sorted(list(word), key=lambda c: ord(c))
        # Convert the sorted characters back to a string
        ordered_word = ''.join(ordered_chars)
        # Add the ordered word to the list of ordered words
        ordered_words.append(ordered_word)
    
    # Join the list of ordered words back into a string, keeping the original spacing
    ordered_string = ' '.join(ordered_words)
    
    return ordered_string
