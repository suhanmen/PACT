def largest_smallest_integers(lst):
    negatives = [x for x in lst if x < 0] # list of negative integers
    positives = [x for x in lst if x > 0] # list of positive integers
    if len(negatives) == 0:
        largest_negative = None
    else:
        largest_negative = max(negatives)
    if len(positives) == 0:
        smallest_positive = None
    else:
        smallest_positive = min(positives)
    return (largest_negative, smallest_positive)
