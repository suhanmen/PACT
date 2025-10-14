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
    lst1_even = all(num % 2 == 0 for num in lst1) # Checks if lst1 is already all even
    lst2_even = any(num % 2 == 0 for num in lst2) # Checks if lst2 has any even numbers
    
    if lst1_even: # If lst1 is already even, return "YES"
        return "YES"
    elif not lst2_even: # If lst2 does not have any even numbers, return "NO"
        return "NO"
    else: # Otherwise, there is a possibility of exchanging elements
        diff = sum(num % 2 == 1 for num in lst1) - sum(num % 2 == 0 for num in lst2) # Calculates the difference in number of odd and even numbers between the two lists
        return "YES" if diff <= 0 else "NO" # If the difference is less than or equal to 0, it is possible to exchange elements and return "YES", otherwise return "NO"
