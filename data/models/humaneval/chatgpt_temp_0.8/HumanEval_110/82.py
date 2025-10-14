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
    # Check if lst1 already consists of only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Find the odd numbers in lst1 and their corresponding even numbers in lst2
    odd_nums = [num for num in lst1 if num % 2 == 1]
    even_nums = [num for num in lst2 if num % 2 == 0]
    
    # If the number of odd numbers in lst1 is greater than the number of even numbers in lst2, it is impossible to make lst1 all even
    if len(odd_nums) > len(even_nums):
        return "NO"
    
    # Otherwise, it is possible to make lst1 all even by exchanging the odd numbers in lst1 with the even numbers in lst2
    return "YES"
