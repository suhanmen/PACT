def sorted_list_sum(lst):
    # create a new list to hold only even-length strings
    new_lst = [word for word in lst if len(word)%2 == 0]
    # sort the new list first by length and then alphabetically
    new_lst.sort(key=lambda x: (len(x), x))
    return new_lst
