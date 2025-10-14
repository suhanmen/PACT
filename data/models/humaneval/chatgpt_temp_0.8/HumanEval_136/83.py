def largest_smallest_integers(lst):
    positive_ints = []
    negative_ints = []
    for num in lst:
        if num > 0:
            positive_ints.append(num)
        elif num < 0:
            negative_ints.append(num)
    max_neg = None
    min_pos = None
    if len(negative_ints) > 0:
        max_neg = max(negative_ints)
    if len(positive_ints) > 0:
        min_pos = min(positive_ints)
    return (max_neg, min_pos)
