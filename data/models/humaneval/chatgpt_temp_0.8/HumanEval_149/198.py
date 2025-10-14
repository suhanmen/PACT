def sorted_list_sum(lst):
    # create a new list to store even length words
    even_length_words = []
    for word in lst:
        # check if the length of the word is even
        if len(word) % 2 == 0:
            even_length_words.append(word)
    # sort the list by length and then by alphabetical order
    sorted_words = sorted(even_length_words, key=lambda x: (len(x), x))
    return sorted_words
