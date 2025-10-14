def sorted_list_sum(lst):
    # filter out strings with odd lengths
    filtered_lst = [word for word in lst if len(word) % 2 == 0]
    # sort the filtered list by ascending length and alphabetically
    sorted_lst = sorted(filtered_lst, key=lambda word: (len(word), word))
    return sorted_lst
