def sort_third(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the indices that are not divisible by three,
    while its values at the indices that are divisible by three are equal
    to the values of the corresponding indices of l, but sorted.
    """
    result = []
    for i in range(len(l)):
        if i % 3 == 0:
            temp_list = l[i:i+3]
            temp_list.sort()
            result.extend(temp_list)
        else:
            result.append(l[i])
    return result
