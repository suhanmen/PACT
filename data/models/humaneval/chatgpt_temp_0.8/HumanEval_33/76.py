def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indices that are not divisible by three, while its values at the indices that are divisible by three are equal
    to the values of the corresponding indices of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    divisible_by_three = [l[i] for i in range(len(l)) if i % 3 == 0]
    divisible_indexes = [i for i in range(len(l)) if i % 3 == 0]
    non_divisible_by_three = [l[i] for i in range(len(l)) if i % 3 != 0]
    divisible_by_three.sort()
    for i in range(len(divisible_by_three)):
        non_divisible_by_three.insert(divisible_indexes[i], divisible_by_three[i])
    return non_divisible_by_three
