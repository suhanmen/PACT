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
    
    # Create a list of even numbers from lst2
    even_nums = [num for num in lst2 if num % 2 == 0]
    
    # Iterate through lst1 and try to replace odd numbers with even numbers from lst2
    for i in range(len(lst1)):
        if lst1[i] % 2 != 0:
            if even_nums:
                lst1[i] = even_nums.pop()
            else:
                return "NO"
    
    # After iterating through lst1, check if it now contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    else:
        return "NO"
