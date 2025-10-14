def sorted_list_sum(lst):
    # Create an empty list to store the even-length words
    even_length_words = []
    # Loop through each string in the input list
    for word in lst:
        # Check if the length of the word is even
        if len(word) % 2 == 0:
            # If it is even, add it to the even_length_words list
            even_length_words.append(word)
    # Sort the list by length and then alphabetically
    even_length_words.sort(key=lambda x: (len(x), x))
    # Return the sorted list
    return even_length_words
