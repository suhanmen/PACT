def exchange(lst1, lst2):
    # Count the number of odd numbers in lst1
    odd_count = sum(1 for x in lst1 if x % 2 == 1)
    
    # Count the number of even numbers in lst2
    even_count = sum(1 for x in lst2 if x % 2 == 0)
    
    # Check if we can make lst1 all even by exchanging elements
    if odd_count <= even_count:
        return "YES"
    else:
        return "NO"
