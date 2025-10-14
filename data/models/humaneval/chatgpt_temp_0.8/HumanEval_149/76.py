def sorted_list_sum(lst):
    # create an empty list to store words with even lengths
    even_length_words = []
    
    # iterate through each word in the list
    for word in lst:
        # check if the length of the word is even
        if len(word) % 2 == 0:
            # if the length is even, add it to the list of even length words
            even_length_words.append(word)
    
    # sort the list of even length words by length and alphabetically if the lengths are equal
    sorted_words = sorted(even_length_words, key=lambda word: (len(word), word))
    
    return sorted_words
