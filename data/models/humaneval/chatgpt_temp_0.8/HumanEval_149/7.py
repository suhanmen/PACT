def sorted_list_sum(lst):
    # create a new list to store words with even lengths
    even_length_words = []
    for word in lst:
        if len(word) % 2 == 0:
            even_length_words.append(word)
    # sort the list by length and then alphabetically
    even_length_words.sort(key=lambda x: (len(x), x))
    return even_length_words
