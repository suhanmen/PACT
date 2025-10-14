def sorted_list_sum(lst):
    # create an empty list to store the even length strings
    even_lst = []
    # iterate over each string in the list
    for s in lst:
        # check if the length of the string is even
        if len(s) % 2 == 0:
            # if the length is even, add it to the even_lst
            even_lst.append(s)
    # sort the even_lst by length and then alphabetically
    sorted_lst = sorted(even_lst, key=lambda x: (len(x), x))
    # return the sorted_lst
    return sorted_lst
