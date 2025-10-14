def sort_third(l: list):
    # create a list of the values at the indices that are divisible by three
    third_values = [l[i] for i in range(len(l)) if i % 3 == 0]
    # sort the third_values list
    sorted_third_values = sorted(third_values)
    # create a new list where the values at the indices that are divisible by three are replaced
    # with the corresponding values from the sorted_third_values list
    result = [sorted_third_values.pop(0) if i % 3 == 0 else l[i] for i in range(len(l))]
    return result
