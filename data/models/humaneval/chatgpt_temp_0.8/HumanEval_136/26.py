def largest_smallest_integers(lst):
    positives = [num for num in lst if num > 0]
    negatives = [num for num in lst if num < 0]
    max_negative = max(negatives) if negatives else None
    min_positive = min(positives) if positives else None
    return (max_negative, min_positive)
