def sorted_list_sum(lst):
    lst = [word for word in lst if len(word) % 2 == 0] # delete odd-length strings
    lst.sort(key=lambda x: (len(x), x)) # sort by length and then alphabetically
    return lst
