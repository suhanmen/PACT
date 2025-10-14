def get_positive(l: list):
    """Return only positive numbers in the list."""
    positive_numbers = []
    for num in l:
        if num > 0:
            positive_numbers.append(num)
    return positive_numbers
