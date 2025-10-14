def sorted_list_sum(lst):
    new_list = []
    for word in lst:
        if len(word) % 2 == 0:
            new_list.append(word)
    sorted_list = sorted(new_list, key=lambda x: (len(x), x))
    return sorted_list
