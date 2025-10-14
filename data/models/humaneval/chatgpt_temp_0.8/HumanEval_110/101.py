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
    lst1_evens = [num for num in lst1 if num % 2 == 0] # create list of evens in lst1
    lst2_evens = [num for num in lst2 if num % 2 == 0] # create list of evens in lst2

    if len(lst1_evens) == len(lst1): # if lst1 already contains only even numbers
        return "YES"
    elif len(lst1_evens) > 0: # if lst1 contains some even numbers
        # find the difference in length between the two even lists
        diff = len(lst1_evens) - len(lst2_evens)
        if diff > 0: # if there are more even numbers in lst1 than lst2
            return "NO"
        else: # if there are fewer or equal even numbers in lst1 than lst2
            return "YES"
    else: # if lst1 contains no even numbers
        return "NO"
