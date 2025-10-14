def sorted_list_sum(lst):
    # remove all strings with odd lengths
    lst = [word for word in lst if len(word) % 2 == 0]
    # sort the list by ascending length and alphabetically
    lst.sort(key=lambda word: (len(word), word))
    return lst
