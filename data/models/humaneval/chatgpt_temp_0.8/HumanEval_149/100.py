def sorted_list_sum(lst):
    lst = [word for word in lst if len(word) % 2 == 0] # filter out strings with odd lengths
    lst = sorted(lst, key=lambda word: (len(word), word)) # sort by length and then alphabetically
    return lst
