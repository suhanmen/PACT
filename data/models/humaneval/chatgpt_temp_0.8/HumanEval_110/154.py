def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    """
    lst1_even = all(x % 2 == 0 for x in lst1)
    if lst1_even:
        return "YES"
    lst2_even = all(x % 2 == 0 for x in lst2)
    if lst2_even:
        return "NO"
    lst1_odd = [x for x in lst1 if x % 2 == 1]
    lst2_even = [x for x in lst2 if x % 2 == 0]
    return "YES" if len(lst1_odd) <= len(lst2_even) else "NO"
