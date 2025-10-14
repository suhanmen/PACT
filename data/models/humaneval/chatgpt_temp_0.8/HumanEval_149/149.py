def sorted_list_sum(lst):
    # create an empty list to store only even length strings
    even_length_strings = []
    for string in lst:
        # check if length of string is even
        if len(string) % 2 == 0:
            even_length_strings.append(string)
    # sort the list by length and alphabetically
    even_length_strings.sort(key=lambda x: (len(x), x))
    return even_length_strings
