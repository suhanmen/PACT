def largest_smallest_integers(lst):
    negatives = [i for i in lst if i < 0]
    positives = [i for i in lst if i > 0]
    
    if not negatives:
        largest_negative = None
    else:
        largest_negative = max(negatives)
    
    if not positives:
        smallest_positive = None
    else:
        smallest_positive = min(positives)
    
    return (largest_negative, smallest_positive)
