def largest_smallest_integers(lst):
    positive_integers = [x for x in lst if x > 0]
    negative_integers = [x for x in lst if x < 0]
    if len(positive_integers) == 0:
        b = None
    else:
        b = min(positive_integers)
    if len(negative_integers) == 0:
        a = None
    else:
        a = max(negative_integers)
    return (a, b)
