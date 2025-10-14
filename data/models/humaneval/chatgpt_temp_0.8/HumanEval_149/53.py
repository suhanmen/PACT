def sorted_list_sum(lst):
    # Create a new list to store the even-length strings
    even_length_lst = []
    for string in lst:
        # Check if the length of the string is even
        if len(string) % 2 == 0:
            even_length_lst.append(string)
    # Sort the even-length strings first by length, then alphabetically
    sorted_lst = sorted(even_length_lst, key=lambda x: (len(x), x))
    return sorted_lst
