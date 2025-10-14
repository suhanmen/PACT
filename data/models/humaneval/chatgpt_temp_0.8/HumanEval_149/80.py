def sorted_list_sum(lst):
    new_lst = []
    for word in lst:
        if len(word) % 2 == 0:
            new_lst.append(word)
    sorted_lst = sorted(new_lst, key=lambda x: (len(x), x))
    return sorted_lst
