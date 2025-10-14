def sorted_list_sum(lst):
    # Create a new list to store the even length strings
    even_length_words = []
    for word in lst:
        if len(word) % 2 == 0:
            even_length_words.append(word)
    # Sort the even length strings by length and then alphabetically
    sorted_words = sorted(even_length_words, key=lambda x: (len(x), x))
    return sorted_words
