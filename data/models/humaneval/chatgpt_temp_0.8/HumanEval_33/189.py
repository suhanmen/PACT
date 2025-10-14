def sort_third(l: list):
    new_l = l[:]  # create a copy of the original list to avoid modifying it directly
    third_indices = [i for i in range(len(l)) if i % 3 == 0]  # get the indices that are divisible by 3
    for i in third_indices:
        new_l[i:i+3] = sorted(new_l[i:i+3])  # sort the values at the divisible-by-3 indices
    return new_l
