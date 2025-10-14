def sorted_list_sum(lst):
    # Create an empty list to store the even length strings
    even_length = []

    # Iterate through each string in the input list
    for string in lst:
        # If the length of the string is even, append it to the even_length list
        if len(string) % 2 == 0:
            even_length.append(string)

    # Sort the even_length list by length (ascending) and alphabetically (if lengths are equal)
    sorted_list = sorted(even_length, key=lambda x: (len(x), x))

    # Return the sorted list
    return sorted_list
