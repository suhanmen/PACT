def sorted_list_sum(lst):
    # remove odd length strings
    lst = [word for word in lst if len(word) % 2 == 0]
    # sort by length and alphabetically
    lst = sorted(lst, key=lambda x: (len(x), x))
    return lst
