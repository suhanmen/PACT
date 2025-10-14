def exchange(lst1, lst2):
    # Find the count of odd numbers in lst1.
    odd_count = sum(1 for num in lst1 if num % 2 != 0)
    
    # Find the count of even numbers in lst2.
    even_count = sum(1 for num in lst2 if num % 2 == 0)
    
    # If there are not enough even numbers in lst2 to replace odd numbers in lst1, return "NO".
    if even_count < odd_count:
        return "NO"
    
    # Otherwise, return "YES".
    return "YES"
