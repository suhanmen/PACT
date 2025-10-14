def sorted_list_sum(lst):
    # Filter out strings with odd length
    filtered_lst = [s for s in lst if len(s) % 2 == 0]
    # Sort by ascending length and then alphabetically
    sorted_lst = sorted(filtered_lst, key=lambda s: (len(s), s))
    return sorted_lst
