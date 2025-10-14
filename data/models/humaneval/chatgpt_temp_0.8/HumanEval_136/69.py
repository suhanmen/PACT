def largest_smallest_integers(lst):
    neg_integers = [i for i in lst if i < 0] # Find all negative integers
    pos_integers = [i for i in lst if i > 0] # Find all positive integers
    a = max(neg_integers) if neg_integers else None # Find the largest negative integer or set to None
    b = min(pos_integers) if pos_integers else None # Find the smallest positive integer or set to None
    return (a, b)
