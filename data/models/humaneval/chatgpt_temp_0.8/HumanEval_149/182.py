python
def sorted_list_sum(lst):
    # create a new list to store the filtered strings
    filtered_lst = []
    for word in lst:
        # check if the length of the word is even
        if len(word) % 2 == 0:
            filtered_lst.append(word)
    # sort the filtered list by length and then alphabetically
    filtered_lst.sort(key=lambda x: (len(x), x))
    return filtered_lst
