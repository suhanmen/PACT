def sorted_list_sum(lst):
    # create a new list that only contains strings with even lengths
    even_lst = [word for word in lst if len(word) % 2 == 0]
    # sort the list by length first
    sorted_lst = sorted(even_lst, key=lambda x: (len(x), x))
    return sorted_lst
