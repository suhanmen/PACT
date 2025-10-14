def sorted_list_sum(lst):
    # Create an empty list to store the even-length words
    even_length_words = []
    
    # Iterate through each word in the list
    for word in lst:
        # Check if the length of the word is even
        if len(word) % 2 == 0:
            # Add the word to the even-length words list
            even_length_words.append(word)
    
    # Sort the even-length words list first by length, then alphabetically
    even_length_words.sort(key=lambda x: (len(x), x))
    
    # Return the sorted even-length words list
    return even_length_words
