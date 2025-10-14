def sorted_list_sum(lst):
    even_length_words = [word for word in lst if len(word) % 2 == 0] # Filter out strings with odd lengths
    sorted_words = sorted(even_length_words, key=lambda x: (len(x), x)) # Sort by length and then alphabetically
    return sorted_words
