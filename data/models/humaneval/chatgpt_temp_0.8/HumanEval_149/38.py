def sorted_list_sum(lst):
    # create a new list to store the even length strings
    even_length_strings = []
    for string in lst:
        # check if the length of the string is even
        if len(string) % 2 == 0:
            even_length_strings.append(string)
    # sort the even length strings based on length and then alphabetically
    even_length_strings.sort(key=lambda x: (len(x), x))
    return even_length_strings
