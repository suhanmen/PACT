def add(lst):
    """Given a non-empty list of integers lst, add the even elements that are at odd indices."""
    
    sum = 0
    for i in range(len(lst)):
        if i % 2 == 1 and lst[i] % 2 == 0:
            sum += lst[i]
    return sum
