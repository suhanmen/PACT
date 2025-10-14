def sorted_list_sum(lst):
    lst = [word for word in lst if len(word) % 2 == 0] # remove odd length strings
    lst = sorted(lst, key=lambda x: (len(x), x)) # sort by ascending length, then alphabetically
    return lst
