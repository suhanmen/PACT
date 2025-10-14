def sorted_list_sum(lst):
    even_length_lst = [word for word in lst if len(word) % 2 == 0]
    return sorted(even_length_lst, key=lambda x: (len(x), x))
