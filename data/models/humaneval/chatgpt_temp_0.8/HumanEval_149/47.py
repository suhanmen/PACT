def sorted_list_sum(lst):
    new_lst = []
    for string in lst:
        if len(string) % 2 == 0:
            new_lst.append(string)
    sorted_lst = sorted(new_lst, key=lambda x: (len(x), x))
    return sorted_lst
