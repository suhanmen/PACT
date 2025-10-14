def sorted_list_sum(lst):
    lst = [x for x in lst if len(x) % 2 == 0]  # delete strings with odd lengths
    lst = sorted(lst, key=lambda x: (len(x), x))  # sort by length and then alphabetically
    return lst
