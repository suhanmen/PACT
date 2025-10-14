def largest_smallest_integers(lst):
    negative_integers = [num for num in lst if num < 0]
    positive_integers = [num for num in lst if num > 0]
    
    if not negative_integers:
        max_negative = None
    else:
        max_negative = max(negative_integers)
    
    if not positive_integers:
        min_positive = None
    else:
        min_positive = min(positive_integers)
    
    return (max_negative, min_positive)
