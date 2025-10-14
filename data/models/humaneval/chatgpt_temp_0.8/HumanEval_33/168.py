def sort_third(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the indices that are not divisible by three, while its values at the indices that are divisible by three are equal
    to the values of the corresponding indices of l, but sorted.
    """
    divisible_by_three = []
    for i in range(len(l)):
        if i % 3 == 0:
            divisible_by_three.append(l[i])
    sorted_divisible_by_three = sorted(divisible_by_three)
    l_prime = []
    for i in range(len(l)):
        if i % 3 == 0:
            l_prime.append(sorted_divisible_by_three.pop(0))
        else:
            l_prime.append(l[i])
    return l_prime
