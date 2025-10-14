def largest_smallest_integers(lst):
    neg_nums = [num for num in lst if num < 0]
    pos_nums = [num for num in lst if num > 0]
    max_neg = min_pos = None
    if neg_nums:
        max_neg = max(neg_nums)
    if pos_nums:
        min_pos = min(pos_nums)
    return (max_neg, min_pos)
