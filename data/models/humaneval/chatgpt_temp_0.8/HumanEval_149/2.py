def sorted_list_sum(lst):
    # filter out strings with odd lengths
    lst = [word for word in lst if len(word) % 2 == 0]
    
    # sort the list based on length and alphabetically if lengths are the same
    lst.sort(key=lambda word: (len(word), word))
    
    return lst
