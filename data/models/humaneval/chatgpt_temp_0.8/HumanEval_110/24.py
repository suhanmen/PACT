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
    # First, check if lst1 is already all even
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # If lst1 is not all even, find the odd numbers in lst1
    odd_nums = [num for num in lst1 if num % 2 != 0]
    
    # Find the even numbers in lst2
    even_nums = [num for num in lst2 if num % 2 == 0]
    
    # If there are enough even numbers in lst2 to replace the odd numbers in lst1, return "YES"
    if len(odd_nums) <= len(even_nums):
        return "YES"
    
    # Otherwise, it is not possible to exchange elements to make lst1 all even, so return "NO"
    return "NO"
