python
def largest_smallest_integers(lst):
    positive = None
    negative = None
    for num in lst:
        if num > 0 and (positive is None or num < positive):
            positive = num
        elif num < 0 and (negative is None or num > negative):
            negative = num
    return (negative, positive)
