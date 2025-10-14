def largest_smallest_integers(lst):
    negative_integers = [i for i in lst if i < 0]
    positive_integers = [i for i in lst if i > 0]
    if len(negative_integers) == 0:
        a = None
    else:
        a = max(negative_integers)
    if len(positive_integers) == 0:
        b = None
    else:
        b = min(positive_integers)
    return (a, b)
