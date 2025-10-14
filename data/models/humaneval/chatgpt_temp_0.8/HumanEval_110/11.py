def exchange(lst1, lst2):
    # Count the number of odd numbers in lst1
    odd_count = sum(1 for x in lst1 if x % 2 != 0)
    
    # Count the number of even numbers in lst2
    even_count = sum(1 for x in lst2 if x % 2 == 0)
    
    # If there are enough even numbers in lst2 to make lst1 all even, return "YES"
    if even_count >= odd_count:
        return "YES"
    else:
        return "NO"
