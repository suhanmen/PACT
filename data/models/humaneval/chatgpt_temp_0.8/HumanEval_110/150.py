def exchange(lst1, lst2):
    # Count the number of odd numbers in lst1
    odd_count = sum([1 for num in lst1 if num % 2 != 0])
    
    # If lst1 already has all even numbers, return "YES"
    if odd_count == 0:
        return "YES"
    
    # Count the number of even numbers in lst2
    even_count = sum([1 for num in lst2 if num % 2 == 0])
    
    # If the number of even numbers in lst2 is greater than or equal to
    # the number of odd numbers in lst1, return "YES"
    if even_count >= odd_count:
        return "YES"
    
    # Otherwise, it is not possible to exchange elements to make lst1 all even
    return "NO"
