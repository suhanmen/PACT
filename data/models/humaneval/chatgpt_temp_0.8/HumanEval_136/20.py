def largest_smallest_integers(lst):
    positive_integers = [num for num in lst if num > 0]
    negative_integers = [num for num in lst if num < 0]
    if positive_integers:
        smallest_positive = min(positive_integers)
    else:
        smallest_positive = None
    if negative_integers:
        largest_negative = max(negative_integers)
    else:
        largest_negative = None
    return (largest_negative, smallest_positive)
