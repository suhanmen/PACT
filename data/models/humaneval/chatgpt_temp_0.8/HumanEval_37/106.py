def sort_even(l: list):
    even_nums = sorted([num for num in l[::2]])
    sorted_list = l.copy() # create a copy of the original list
    sorted_list[::2] = even_nums # replace even indices with sorted even numbers
    return sorted_list
