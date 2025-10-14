def sorted_list_sum(lst):
    lst = [word for word in lst if len(word) % 2 == 0] # deletes strings with odd lengths
    lst = sorted(lst, key=lambda x: (len(x), x)) # sorts the list by length and alphabetically
    return lst
