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
    
    # Get indices of odd numbers in lst1
    odd_indices = [i for i, num in enumerate(lst1) if num % 2 != 0]
    
    # Check if there are any odd numbers in lst2
    if any(num % 2 != 0 for num in lst2):
        return "NO"
    
    # Iterate over odd indices and try to find a corresponding even number in lst2
    for i in odd_indices:
        for j, num in enumerate(lst2):
            if num % 2 == 0:
                # Swap the odd number in lst1 with the even number in lst2
                lst1[i], lst2[j] = lst2[j], lst1[i]
                # Check if lst1 now contains only even numbers
                if all(num % 2 == 0 for num in lst1):
                    return "YES"
    
    return "NO"
