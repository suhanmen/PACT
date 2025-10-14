def sorted_list_sum(lst):
    # create a new list to store even length strings
    even_lst = []
    for string in lst:
        if len(string) % 2 == 0:
            even_lst.append(string)
    # sort the even length strings by length first, then alphabetically
    sorted_lst = sorted(even_lst, key=lambda x: (len(x), x))
    return sorted_lst
