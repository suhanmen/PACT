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
    if all(x % 2 == 0 for x in lst1):
        return "YES"
    
    # Find all the even numbers in lst2
    evens_lst2 = [x for x in lst2 if x % 2 == 0]
    
    # Sort lst1 in decreasing order of odd numbers
    odds_lst1 = sorted([x for x in lst1 if x % 2 != 0], reverse=True)
    
    # Iterate through the odd numbers in lst1 and try to exchange them
    for odd in odds_lst1:
        for i, even in enumerate(evens_lst2):
            if even > odd:
                lst1[lst1.index(odd)] = even
                lst2[i] = odd
                evens_lst2.pop(i)
                break
        else:
            continue
        break
    
    # Check if lst1 now contains only even numbers
    if all(x % 2 == 0 for x in lst1):
        return "YES"
    else:
        return "NO"
