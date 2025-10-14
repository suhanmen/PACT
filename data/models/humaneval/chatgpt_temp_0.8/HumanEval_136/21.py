def largest_smallest_integers(lst):
    pos_integers = [num for num in lst if num > 0]
    neg_integers = [num for num in lst if num < 0]
    max_neg = None if len(neg_integers) == 0 else max(neg_integers)
    min_pos = None if len(pos_integers) == 0 else min(pos_integers)
    return (max_neg, min_pos)
