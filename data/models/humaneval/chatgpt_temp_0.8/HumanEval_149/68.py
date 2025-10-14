def sorted_list_sum(lst):
    new_lst = []
    for word in lst:
        if len(word) % 2 == 0:
            new_lst.append(word)
    return sorted(new_lst, key=lambda x: (len(x), x))
