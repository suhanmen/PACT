def sorted_list_sum(lst):
    # create a new list to store even-length strings
    new_lst = []
    for word in lst:
        # check if the length of the word is even
        if len(word) % 2 == 0:
            new_lst.append(word)
    # sort the list by length and alphabetically
    new_lst.sort(key=lambda x: (len(x), x))
    return new_lst
