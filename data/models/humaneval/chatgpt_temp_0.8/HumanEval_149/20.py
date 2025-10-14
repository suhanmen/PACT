def sorted_list_sum(lst):
    # create a list of strings with even lengths only
    even_length_strings = [s for s in lst if len(s) % 2 == 0]
    # sort the list by length and then alphabetically
    sorted_list = sorted(even_length_strings, key=lambda s: (len(s), s))
    return sorted_list
