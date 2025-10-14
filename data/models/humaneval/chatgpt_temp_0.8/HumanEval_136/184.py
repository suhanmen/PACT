def largest_smallest_integers(lst):
    negative = [i for i in lst if i < 0]
    positive = [i for i in lst if i > 0]
    
    if negative:
        largest_negative = max(negative)
    else:
        largest_negative = None
        
    if positive:
        smallest_positive = min(positive)
    else:
        smallest_positive = None
        
    return (largest_negative, smallest_positive)
