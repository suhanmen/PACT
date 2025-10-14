def sorted_list_sum(lst):
    # Create an empty list to store the words with even lengths
    even_length_words = []
    
    # Iterate through the input list
    for word in lst:
        # Check if the length of the word is even
        if len(word) % 2 == 0:
            # If the length is even, add the word to the even_length_words list
            even_length_words.append(word)
    
    # Sort the even_length_words list by length and then alphabetically
    even_length_words.sort(key=lambda x: (len(x), x))
    
    # Return the sorted even_length_words list
    return even_length_words
