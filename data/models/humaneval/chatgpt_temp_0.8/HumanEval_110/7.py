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
    # Check if lst1 already contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    # Iterate through lst2 and try to find elements to exchange with lst1
    for num in lst2:
        if num % 2 == 0:
            lst1.append(num) # add even number to lst1
            lst2.remove(num) # remove even number from lst2
            # Check if lst1 now contains only even numbers
            if all(num % 2 == 0 for num in lst1):
                return "YES"
    # If all elements of lst2 have been checked and lst1 still doesn't contain only even numbers, return "NO"
    return "NO"
