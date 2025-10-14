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
    
    # Get the odd numbers from lst1
    odds = [num for num in lst1 if num % 2 == 1]
    
    # Try to exchange the odd numbers with even numbers from lst2
    for i in range(len(lst2)):
        if lst2[i] % 2 == 0 and lst2[i] not in lst1:
            lst1[lst1.index(odds[0])] = lst2[i]
            odds.pop(0)
            if all(num % 2 == 0 for num in lst1):
                return "YES"
            if not odds:
                break
    
    # Check if lst1 is now all even
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    else:
        return "NO"
