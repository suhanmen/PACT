def largest_smallest_integers(lst):
    positives = [x for x in lst if x > 0]
    negatives = [x for x in lst if x < 0]
    
    max_negative = None
    min_positive = None
    
    if negatives:
        max_negative = max(negatives)
    if positives:
        min_positive = min(positives)
        
    return (max_negative, min_positive)
