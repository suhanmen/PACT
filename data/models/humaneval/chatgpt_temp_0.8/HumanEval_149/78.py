def sorted_list_sum(lst):
    # create a list to store even length words
    even_len_words = []
    
    # loop through each word in the input list
    for word in lst:
        # check if the length of the word is even
        if len(word) % 2 == 0:
            # if it is even, add it to the list of even length words
            even_len_words.append(word)
    
    # sort the list of even length words by length and then alphabetically
    sorted_words = sorted(even_len_words, key=lambda x: (len(x), x))
    
    # return the sorted list of even length words
    return sorted_words
