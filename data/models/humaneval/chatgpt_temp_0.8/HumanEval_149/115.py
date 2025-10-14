def sorted_list_sum(lst):
    # Create an empty list to store the even length words
    even_length_words = []
    # Iterate through each word in the list
    for word in lst:
        # If the length of the word is even, append it to the even_length_words list
        if len(word) % 2 == 0:
            even_length_words.append(word)
    # Sort the even_length_words list first by length and then by alphabetical order
    even_length_words.sort(key=lambda x: (len(x), x))
    # Return the sorted list
    return even_length_words
