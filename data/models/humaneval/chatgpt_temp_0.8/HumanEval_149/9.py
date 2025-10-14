def sorted_list_sum(lst):
    # Remove strings with odd lengths
    lst = [word for word in lst if len(word) % 2 == 0]
    # Sort the list by ascending length and alphabetically if the lengths are the same
    lst.sort(key=lambda x: (len(x), x))
    return lst
