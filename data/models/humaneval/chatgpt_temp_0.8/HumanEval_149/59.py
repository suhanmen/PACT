def sorted_list_sum(lst):
    # Create a new list to store even-length words
    even_words = []
    for word in lst:
        # Check if word length is even
        if len(word) % 2 == 0:
            even_words.append(word)
    # Sort the even-length words by length and then alphabetically
    even_words.sort(key=lambda x: (len(x), x))
    return even_words
