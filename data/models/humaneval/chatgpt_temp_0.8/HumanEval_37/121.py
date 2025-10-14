def sort_even(l: list):
    even_indices = [i for i in range(len(l)) if i % 2 == 0] # find even indices
    even_values = [l[i] for i in even_indices] # get even values
    even_values.sort() # sort even values
    sorted_l = l.copy() # make a copy of l to preserve the original list
    for i in even_indices:
        sorted_l[i] = even_values.pop(0) # replace even indices with sorted even values
    return sorted_l
