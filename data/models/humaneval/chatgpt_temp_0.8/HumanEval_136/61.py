def largest_smallest_integers(lst):
    negatives = []
    positives = []
    for num in lst:
        if num < 0:
            negatives.append(num)
        elif num > 0:
            positives.append(num)
    if not negatives:
        largest_negative = None
    else:
        largest_negative = max(negatives)
    if not positives:
        smallest_positive = None
    else:
        smallest_positive = min(positives)
    return (largest_negative, smallest_positive)
