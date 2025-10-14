def sorted_list_sum(lst):
    # create a new list to hold the even-length strings
    even_lst = []
    for word in lst:
        # check if word length is even
        if len(word) % 2 == 0:
            even_lst.append(word)
    # sort the even-length list by length and then alphabetically
    sorted_lst = sorted(even_lst, key=lambda x: (len(x), x))
    return sorted_lst
