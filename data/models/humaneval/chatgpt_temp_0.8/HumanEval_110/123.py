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
    # Check if lst1 is already all even
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Find all odd numbers in lst1
    odd_nums = [num for num in lst1 if num % 2 != 0]
    
    # Find all even numbers in lst2
    even_nums = [num for num in lst2 if num % 2 == 0]
    
    # If there are not enough even numbers in lst2 to replace the odd numbers in lst1, return "NO"
    if len(odd_nums) > len(even_nums):
        return "NO"
    
    # Sort the lists in ascending order
    odd_nums.sort()
    even_nums.sort()
    
    # Replace the odd numbers in lst1 with even numbers from lst2
    for i in range(len(odd_nums)):
        lst1[lst1.index(odd_nums[i])] = even_nums[i]
    
    # Check if lst1 is now all even
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    else:
        return "NO"
