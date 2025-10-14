def largest_smallest_integers(lst):
    positive_integers = [i for i in lst if i > 0]
    negative_integers = [i for i in lst if i < 0]

    max_negative_int = None
    min_positive_int = None

    if negative_integers:
        max_negative_int = max(negative_integers)

    if positive_integers:
        min_positive_int = min(positive_integers)

    return (max_negative_int, min_positive_int)
