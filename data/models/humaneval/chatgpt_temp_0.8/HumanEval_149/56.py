def sorted_list_sum(lst):
    # Create an empty list to store the even-length strings
    even_lst = []
    for word in lst:
        # Check if the length of the string is even
        if len(word) % 2 == 0:
            even_lst.append(word)
    # Sort the even-length strings by length and then alphabetically
    even_lst.sort(key=lambda x: (len(x), x))
    return even_lst
