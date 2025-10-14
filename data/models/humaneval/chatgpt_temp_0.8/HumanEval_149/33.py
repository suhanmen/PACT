def sorted_list_sum(lst):
    # create a new list and add only even length words
    new_lst = [word for word in lst if len(word) % 2 == 0]
    
    # sort the list by length and alphabetically
    new_lst.sort(key=lambda word: (len(word), word))
    
    return new_lst
