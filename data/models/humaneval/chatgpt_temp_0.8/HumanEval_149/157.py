def sorted_list_sum(lst):
    # Create a new list to store the words with even lengths
    even_length_words = []
    for word in lst:
        if len(word) % 2 == 0:
            even_length_words.append(word)
    # Sort the list by length, then alphabetically
    sorted_list = sorted(even_length_words, key=lambda s: (len(s), s))
    return sorted_list
