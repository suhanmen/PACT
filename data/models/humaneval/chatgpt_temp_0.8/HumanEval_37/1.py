def sort_even(l: list):
    even_indices = [i for i in range(len(l)) if i % 2 == 0] # get the even indices of the list
    even_values = [l[i] for i in even_indices] # get the even values of the list
    even_values.sort() # sort the even values
    sorted_list = l.copy() # create a copy of the original list
    for i in even_indices:
        sorted_list[i] = even_values[i//2] # replace the even values with the sorted even values
    return sorted_list
