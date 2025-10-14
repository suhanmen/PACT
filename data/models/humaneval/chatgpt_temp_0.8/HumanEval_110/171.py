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
    # Check if lst1 already contains all even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Get the indices of odd numbers in lst1
    odd_indices = [i for i in range(len(lst1)) if lst1[i] % 2 != 0]
    
    # Loop through odd indices and see if they can be swapped with an even number from lst2
    for i in odd_indices:
        for j in range(len(lst2)):
            if lst2[j] % 2 == 0:
                lst1[i], lst2[j] = lst2[j], lst1[i]
                if all(num % 2 == 0 for num in lst1):
                    return "YES"
                else:
                    # Swap back and continue searching
                    lst1[i], lst2[j] = lst2[j], lst1[i]
    
    # If all odd numbers in lst1 cannot be swapped with an even number from lst2, return "NO"
    return "NO"
