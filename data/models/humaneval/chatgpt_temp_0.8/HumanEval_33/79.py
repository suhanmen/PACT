def sort_third(l: list):
    # Get the values that are divisible by 3 and sort them
    divisible_by_3 = sorted([l[i] for i in range(len(l)) if i % 3 == 0])
    # Build the sorted list
    sorted_l = [divisible_by_3.pop(0) if i % 3 == 0 else l[i] for i in range(len(l))]
    return sorted_l
