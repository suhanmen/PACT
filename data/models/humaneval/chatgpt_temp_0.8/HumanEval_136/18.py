def largest_smallest_integers(lst):
    negative_integers = [num for num in lst if num < 0]
    positive_integers = [num for num in lst if num > 0]
    largest_negative = None if len(negative_integers) == 0 else max(negative_integers)
    smallest_positive = None if len(positive_integers) == 0 else min(positive_integers)
    return (largest_negative, smallest_positive)
