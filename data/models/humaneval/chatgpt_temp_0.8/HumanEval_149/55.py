python
def sorted_list_sum(lst):
    # create a new list to store the filtered words
    filtered_lst = []
    for word in lst:
        # if the length of the word is even, add it to the new list
        if len(word) % 2 == 0:
            filtered_lst.append(word)
    # sort the filtered list first by length, then alphabetically
    filtered_lst.sort(key=lambda x: (len(x), x))
    return filtered_lst
