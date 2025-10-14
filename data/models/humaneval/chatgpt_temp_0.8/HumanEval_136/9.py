def largest_smallest_integers(lst):
    negative_integers = [num for num in lst if num < 0]
    positive_integers = [num for num in lst if num > 0]
    
    largest_negative = None
    smallest_positive = None
    
    if negative_integers:
        largest_negative = max(negative_integers)
    if positive_integers:
        smallest_positive = min(positive_integers)
    
    return (largest_negative, smallest_positive)
