python
def largest_smallest_integers(lst):
    pos = [i for i in lst if i > 0]
    neg = [i for i in lst if i < 0]
    return (max(neg, default=None), min(pos, default=None))
