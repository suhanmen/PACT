def largest_smallest_integers(lst):
    positive_ints = [i for i in lst if i > 0]
    negative_ints = [i for i in lst if i < 0]
    if not positive_ints:
        b = None
    else:
        b = min(positive_ints)
    if not negative_ints:
        a = None
    else:
        a = max(negative_ints)
    return (a, b)
