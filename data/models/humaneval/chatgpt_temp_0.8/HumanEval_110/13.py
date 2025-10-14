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
    # First, check if lst1 already contains all even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # If not, try to find odd elements in lst1 that can be replaced with even elements in lst2
    odd_indices = [i for i in range(len(lst1)) if lst1[i] % 2 != 0]
    for index in odd_indices:
        for i in range(len(lst2)):
            if lst2[i] % 2 == 0:
                # Replace odd element in lst1 with even element in lst2 and check if lst1 is all even
                lst1[index] = lst2[i]
                if all(num % 2 == 0 for num in lst1):
                    return "YES"
    
    # If no exchange was successful, return "NO"
    return "NO"
