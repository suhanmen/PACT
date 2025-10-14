def sort_third(l: list):
    # create a new list to store the sorted values
    sorted_values = sorted(l[::3])
    
    # iterate over the original list and update it in place
    for i in range(len(l)):
        if i % 3 == 0:
            # use the corresponding value from the sorted list
            l[i] = sorted_values.pop(0)
    
    return l
