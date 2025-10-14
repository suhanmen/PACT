def largest_smallest_integers(lst):
    negative, positive = [], []
    for num in lst:
        if num < 0:
            negative.append(num)
        elif num > 0:
            positive.append(num)
    if not negative:
        largest = None
    else:
        largest = max(negative)
    if not positive:
        smallest = None
    else:
        smallest = min(positive)
    return (largest, smallest)
