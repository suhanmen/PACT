def sorted_list_sum(lst):
    # Create a new list with only even length strings
    new_lst = [word for word in lst if len(word) % 2 == 0]
    # Sort the list first by length, then alphabetically
    sorted_lst = sorted(new_lst, key=lambda x: (len(x), x))
    return sorted_lst
