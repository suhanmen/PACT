def largest_smallest_integers(lst):
    negative_ints = [x for x in lst if x < 0]
    positive_ints = [x for x in lst if x > 0]
    if negative_ints:
        largest_negative = max(negative_ints)
    else:
        largest_negative = None
    if positive_ints:
        smallest_positive = min(positive_ints)
    else:
        smallest_positive = None
    return (largest_negative, smallest_positive)
