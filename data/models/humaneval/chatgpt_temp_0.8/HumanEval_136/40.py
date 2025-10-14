def largest_smallest_integers(lst):
    neg_integers = [num for num in lst if num < 0]
    pos_integers = [num for num in lst if num > 0]
    a = max(neg_integers) if len(neg_integers) > 0 else None
    b = min(pos_integers) if len(pos_integers) > 0 else None
    return (a, b)
