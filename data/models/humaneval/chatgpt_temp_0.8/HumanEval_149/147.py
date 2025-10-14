def sorted_list_sum(lst):
    lst = [word for word in lst if len(word) % 2 == 0] # Remove strings with odd lengths
    lst = sorted(lst, key=lambda x: (len(x), x)) # Sort by length and then alphabetically
    return lst
