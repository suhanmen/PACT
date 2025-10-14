def largest_smallest_integers(lst):
    positive_integers = [i for i in lst if i > 0]
    negative_integers = [i for i in lst if i < 0]
    
    if positive_integers:
        smallest_positive = min(positive_integers)
    else:
        smallest_positive = None
    
    if negative_integers:
        largest_negative = max(negative_integers)
    else:
        largest_negative = None
    
    return (largest_negative, smallest_positive)
