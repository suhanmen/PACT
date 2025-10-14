def largest_smallest_integers(lst):
    negative_integers = [n for n in lst if n < 0]
    positive_integers = [n for n in lst if n > 0]
    if not negative_integers:
        largest_negative = None
    else:
        largest_negative = max(negative_integers)
    if not positive_integers:
        smallest_positive = None
    else:
        smallest_positive = min(positive_integers)
    return (largest_negative, smallest_positive)
