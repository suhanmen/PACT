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
    # Check if all elements of lst1 are already even
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Find the even elements in lst2 that can be exchanged with odd elements in lst1
    exchange_elements = [num for num in lst2 if num % 2 == 0 and num not in lst1]
    
    # If there are not enough exchangeable elements, return "NO"
    if len(exchange_elements) < lst1.count(1) - lst1.count(2):
        return "NO"
    
    # Perform the exchanges and check if lst1 is all even
    for i in range(len(lst1)):
        if lst1[i] % 2 != 0:
            for j in range(len(exchange_elements)):
                if exchange_elements[j] % 2 == 0:
                    lst1[i], exchange_elements[j] = exchange_elements[j], lst1[i]
                    break
            else:
                return "NO"
        if all(num % 2 == 0 for num in lst1):
            return "YES"
    
    return "NO"
