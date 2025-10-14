def sort_third(l: list):
    # Split the original list into three sublists
    sublists = [l[i:i+3] for i in range(0, len(l), 3)]
    # Sort the third sublist of each group
    for sublist in sublists:
        if len(sublist) == 3:
            sublist[2] = sorted(sublist[2])
    # Merge the sublists back into a single list
    l_sorted = [item for sublist in sublists for item in sublist]
    return l_sorted
