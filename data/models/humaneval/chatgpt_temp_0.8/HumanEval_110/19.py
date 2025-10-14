def exchange(lst1, lst2):
    """
    In this problem, you will implement a function that takes two lists of numbers,
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
    # First, check if all elements of lst1 are already even
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # If not, check if there are odd elements in lst2 that can be swapped with even elements in lst1
    for num1 in lst1:
        if num1 % 2 == 0:
            continue
        for num2 in lst2:
            if num2 % 2 
