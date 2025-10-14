def sorted_list_sum(lst):
    # filtering out odd length strings
    even_length_strings = [word for word in lst if len(word) % 2 == 0]
    
    # sorting strings based on length and then alphabetically
    sorted_strings = sorted(even_length_strings, key=lambda x: (len(x), x))
    
    return sorted_strings
