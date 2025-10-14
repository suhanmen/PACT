def sorted_list_sum(lst):
    # filter out odd-length strings
    lst = [word for word in lst if len(word) % 2 == 0]
    # sort by length and then alphabetically
    lst.sort(key=lambda x: (len(x), x))
    return lst
