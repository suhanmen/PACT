def sorted_list_sum(lst):
    even_lst = [word for word in lst if len(word) % 2 == 0]
    sorted_lst = sorted(even_lst, key=lambda x: (len(x), x))
    return sorted_lst
