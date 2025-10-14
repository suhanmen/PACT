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
    # Find all the odd numbers in lst1
    odd_nums = [num for num in lst1 if num % 2 != 0]
    
    # Find all the even numbers in lst2
    even_nums = [num for num in lst2 if num % 2 == 0]
    
    # If there are not enough even numbers in lst2 to replace all the odd numbers in lst1, return "NO"
    if len(odd_nums) > len(even_nums):
        return "NO"
    
    # Otherwise, sort the even numbers in descending order and replace the odd numbers in lst1 with them
    even_nums.sort(reverse=True)
    for i in range(len(lst1)):
        if lst1[i] % 2 != 0:
            lst1[i] = even_nums.pop(0)
    
    # Check if lst1 contains only even numbers, and return "YES" or "NO" accordingly
    for num in lst1:
        if num % 2 != 0:
            return "NO"
    return "YES"
