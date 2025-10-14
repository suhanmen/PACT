def sorted_list_sum(lst):
    # create a new list with only elements of even length
    even_lst = [word for word in lst if len(word) % 2 == 0]
    # sort the even_lst by length and then alphabetically
    sorted_lst = sorted(even_lst, key=lambda x: (len(x), x))
    return sorted_lst
