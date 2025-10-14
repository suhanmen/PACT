def sort_third(l: list):
    # create a new list with the same elements as l
    new_list = l[:]
    # get the indices that are divisible by three
    indices = [i for i in range(len(l)) if i % 3 == 0]
    # sort the values at the divisible indices
    sorted_values = sorted([l[i] for i in indices])
    # replace the values at the divisible indices with their sorted values
    for i in indices:
        new_list[i] = sorted_values.pop(0)
    return new_list
