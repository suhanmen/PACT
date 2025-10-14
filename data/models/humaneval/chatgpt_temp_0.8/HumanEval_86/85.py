def anti_shuffle(s):
    words = s.split() # Split the string into words
    ordered_words = [] # Empty list to store ordered words
    for word in words:
        ordered_word = ''.join(sorted(word)) # Sort the characters in each word based on ascii value
        ordered_words.append(ordered_word) # Add the ordered word to the list
    return ' '.join(ordered_words) # Join the ordered words with spaces and return the final string
