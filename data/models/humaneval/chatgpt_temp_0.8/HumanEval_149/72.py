def sorted_list_sum(lst):
    lst = [word for word in lst if len(word) % 2 == 0] # delete strings with odd lengths
    lst.sort(key=lambda word: (len(word), word)) # sort by ascending length and then alphabetically
    return lst
