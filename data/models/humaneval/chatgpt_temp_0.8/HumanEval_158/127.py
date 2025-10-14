def find_max(words):
    # Create an empty dictionary to store the unique characters count for each word
    unique_char_count = {}
    
    # Iterate through each word in the list
    for word in words:
        # Create a set of unique characters in the word and count them
        unique_chars = set(word)
        count = len(unique_chars)
        
        # Add the count to the dictionary with the word as the key
        unique_char_count[word] = count
        
    # Find the maximum count in the dictionary
    max_count = max(unique_char_count.values())
    
    # Create a list of words with the maximum count
    max_words = [word for word, count in unique_char_count.items() if count == max_count]
    
    # Sort the list lexicographically and return the first word
    max_words.sort()
    return max_words[0] if max_words else ""
