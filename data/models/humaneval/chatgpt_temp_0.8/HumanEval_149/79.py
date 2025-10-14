def sorted_list_sum(lst):
    # Create a new list to store even length strings
    even_lst = []
    for string in lst:
        # Check if string has even length
        if len(string) % 2 == 0:
            even_lst.append(string)
    # Sort the list by ascending length of each word and alphabetical order
    sorted_lst = sorted(even_lst, key=lambda x: (len(x), x))
    return sorted_lst
