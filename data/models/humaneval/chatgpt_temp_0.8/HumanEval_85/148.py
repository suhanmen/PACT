def add(lst):
    """Given a non-empty list of integers lst, add the even elements that are at odd indices."""
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0])
