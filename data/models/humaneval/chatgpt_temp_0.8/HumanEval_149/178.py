def sorted_list_sum(lst):
    # Create a new list to store even-length strings
    even_lst = []
    for word in lst:
        # Check if the length of the word is even
        if len(word) % 2 == 0:
            even_lst.append(word)
    # Sort the even-length strings by length and alphabetically
    sorted_lst = sorted(even_lst, key=lambda word: (len(word), word))
    return sorted_lst
