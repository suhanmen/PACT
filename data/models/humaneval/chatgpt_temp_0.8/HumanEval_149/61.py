def sorted_list_sum(lst):
    evens = []
    for string in lst:
        if len(string) % 2 == 0:
            evens.append(string)
    return sorted(evens, key=lambda x: (len(x), x))
