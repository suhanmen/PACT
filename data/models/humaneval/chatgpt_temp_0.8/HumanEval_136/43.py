def largest_smallest_integers(lst):
    positive_integers = []
    negative_integers = []
    for num in lst:
        if num > 0:
            positive_integers.append(num)
        elif num < 0:
            negative_integers.append(num)
    if positive_integers:
        b = min(positive_integers)
    else:
        b = None
    if negative_integers:
        a = max(negative_integers)
    else:
        a = None
    return (a, b)
