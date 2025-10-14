def largest_smallest_integers(lst):
    negatives = [num for num in lst if num < 0]
    positives = [num for num in lst if num > 0]
    
    if not negatives:
        largest = None
    else:
        largest = max(negatives)
        
    if not positives:
        smallest = None
    else:
        smallest = min(positives)
    
    return (largest, smallest)
