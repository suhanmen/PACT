def sorted_list_sum(lst):
    # create a new list to store the even-length words
    even_words = []
    for word in lst:
        if len(word) % 2 == 0:
            even_words.append(word)
    
    # sort the even-length words by length and then alphabetically
    sorted_words = sorted(even_words, key=lambda word: (len(word), word))
    
    return sorted_words
