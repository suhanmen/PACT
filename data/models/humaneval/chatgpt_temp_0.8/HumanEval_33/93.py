def sort_third(l: list):
    # Create a list to store the values at indices divisible by 3
    third_indices = []
    for i in range(len(l)):
        if i % 3 == 0:
            third_indices.append(l[i])
    # Sort the list of values at indices divisible by 3
    third_indices.sort()
    # Create a new list with the sorted values at the corresponding indices
    new_list = []
    for i in range(len(l)):
        if i % 3 == 0:
            new_list.append(third_indices.pop(0))
        else:
            new_list.append(l[i])
    return new_list
