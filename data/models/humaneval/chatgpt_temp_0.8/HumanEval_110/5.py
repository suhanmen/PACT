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
    # Check if all elements in lst1 are already even
    if all(num % 2 == 0 for num in lst1):
        return "YES"

    # If not, check if there are odd numbers in lst2 that can be swapped with even numbers in lst1
    for num in lst2:
        if num % 2 == 0 and (num not in lst1):
            continue
        elif num % 2 == 1:
            for i in range(len(lst1)):
                if lst1[i] % 2 == 0 and (lst1[i] not in lst2):
                    # Swap the elements
                    lst1[i], num = num, lst1[i]
                    break

    # Check if all elements in lst1 are now even
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    else:
        return "NO"
