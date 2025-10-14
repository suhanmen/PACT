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
    # check if lst1 already has all even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # find the even numbers in lst2
    even_nums = [num for num in lst2 if num % 2 == 0]
    
    # check if there are enough even numbers in lst2 to replace odd numbers in lst1
    if len(even_nums) < (len(lst1) - lst1.count('even')):
        return "NO"
    
    # replace odd numbers in lst1 with even numbers from lst2
    for i in range(len(lst1)):
        if lst1[i] % 2 != 0:
            lst1[i] = even_nums.pop()
            if len(even_nums) == 0:
                break
    
    # check if lst1 now only contains even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    return "NO"
