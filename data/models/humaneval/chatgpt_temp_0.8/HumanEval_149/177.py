def sorted_list_sum(lst):
    # Remove strings with odd length
    lst = [word for word in lst if len(word) % 2 == 0]

    # Sort by length and then alphabetically
    lst = sorted(lst, key=lambda x: (len(x), x))

    return lst
