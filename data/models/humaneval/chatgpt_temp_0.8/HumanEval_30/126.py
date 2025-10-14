def get_positive(l: list):
    """Return only positive numbers in the list."""
    positive_nums = []
    for num in l:
        if num > 0:
            positive_nums.append(num)
    return positive_nums
