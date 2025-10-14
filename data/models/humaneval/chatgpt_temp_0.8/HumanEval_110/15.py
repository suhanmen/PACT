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
    # Check if all elements in lst1 are even
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Check if there are any even numbers in lst2 to exchange with lst1
    if not any(num % 2 == 0 for num in lst2):
        return "NO"
    
    # Exchange even numbers in lst2 with odd numbers in lst1
    for i in range(len(lst1)):
        if lst1[i] % 2 != 0:
            for j in range(len(lst2)):
                if lst2[j] % 2 == 0:
                    lst1[i], lst2[j] = lst2[j], lst1[i]
                    break
    
    # Check if all elements in lst1 are even after the exchange
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    else:
        return "NO"
