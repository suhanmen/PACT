def sorted_list_sum(lst):
    # Remove strings with odd lengths
    lst = [word for word in lst if len(word) % 2 == 0]

    # Sort strings by length, then alphabetically
    lst.sort(key=lambda word: (len(word), word))

    return lst
