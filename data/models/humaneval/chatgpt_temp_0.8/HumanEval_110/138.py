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
    
    # Calculate the sum of odd numbers in lst1
    odd_sum = sum(num for num in lst1 if num % 2 != 0)
    
    # Loop through the elements in lst2 to find a pair that can be exchanged
    for num2 in lst2:
        # If the sum of odd numbers in lst1 plus the current element in lst2 is even
        # and lst1 without the current element and with the exchanged element is all even
        if (odd_sum + num2) % 2 == 0 and all((num != lst1[0] or idx == 0) and num % 2 == 0 for idx, num in enumerate(lst1[1:] + [num2])):
            return "YES"
    
    # If no pair can be exchanged, return "NO"
    return "NO"
