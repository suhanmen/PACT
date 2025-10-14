def exchange(lst1, lst2):
    # Check if lst1 already contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Count the number of odd numbers in lst1
    odd_count = sum(1 for num in lst1 if num % 2 == 1)
    
    # Count the number of even numbers in lst2
    even_count = sum(1 for num in lst2 if num % 2 == 0)
    
    # If there are enough even numbers in lst2 to replace all odd numbers in lst1
    if even_count >= odd_count:
        return "YES"
    else:
        return "NO"
