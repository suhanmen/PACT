def sorted_list_sum(lst):
    # create a list to store words with even lengths
    even_length_words = []
    
    # iterate through each word in the input list
    for word in lst:
        # check if the length of the word is even
        if len(word) % 2 == 0:
            # if so, add it to the list of even length words
            even_length_words.append(word)
    
    # sort the list of even length words first by length, then by alphabetical order
    sorted_words = sorted(even_length_words, key=lambda x: (len(x), x))
    
    # return the sorted list of words
    return sorted_words
