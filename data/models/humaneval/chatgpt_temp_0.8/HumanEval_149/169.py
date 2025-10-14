def sorted_list_sum(lst):
    lst = [word for word in lst if len(word) % 2 == 0] # Delete strings with odd lengths
    lst.sort(key=lambda x: (len(x), x)) # Sort by ascending length first, then alphabetical order
    return lst
