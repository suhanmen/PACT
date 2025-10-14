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
    
    # Find the odd numbers in lst1 and the even numbers in lst2
    lst1_odd = [num for num in lst1 if num % 2 != 0]
    lst2_even = [num for num in lst2 if num % 2 == 0]
    
    # Check if there are enough even numbers in lst2 to replace the odd numbers in lst1
    if len(lst1_odd) > len(lst2_even):
        return "NO"
    
    # If there are enough even numbers, replace the odd numbers in lst1 with even numbers from lst2
    for i in range(len(lst1)):
        if lst1[i] % 2 != 0:
            lst1[i] = lst2_even.pop(0)
    
    # Check if lst1 is now all even
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    else:
        return "NO"
