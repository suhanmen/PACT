def sorted_list_sum(lst):
    # create a new list with only even-length strings
    even_len_lst = [s for s in lst if len(s) % 2 == 0]
    # sort the even-length list by length and then alphabetically
    sorted_lst = sorted(even_len_lst, key=lambda s: (len(s), s))
    return sorted_lst
