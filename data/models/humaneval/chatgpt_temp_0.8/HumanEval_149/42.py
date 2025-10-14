def sorted_list_sum(lst):
    # Delete strings with odd lengths from the list
    lst = [word for word in lst if len(word) % 2 == 0]
    # Sort the list by ascending length and then alphabetically if words have the same length
    lst.sort(key=lambda x: (len(x), x))
    return lst
