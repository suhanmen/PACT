def sorted_list_sum(lst):
    # create an empty list to store the even length strings
    even_lst = []
    for word in lst:
        # check if the length of the word is even
        if len(word) % 2 == 0:
            even_lst.append(word)
    # sort the list by length and alphabetically
    even_lst.sort(key=lambda x: (len(x), x))
    return even_lst
