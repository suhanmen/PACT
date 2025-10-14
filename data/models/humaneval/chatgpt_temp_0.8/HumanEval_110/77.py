def exchange(lst1, lst2):
    # Count number of odd elements in lst1
    odd_count = sum(1 for num in lst1 if num % 2 == 1)

    # If there are no odd elements in lst1, return "YES"
    if odd_count == 0:
        return "YES"
    
    # Check if there are enough even elements in lst2 to replace odd elements in lst1
    even_count = sum(1 for num in lst2 if num % 2 == 0)
    if even_count < odd_count:
        return "NO"

    # If there are enough even elements in lst2, return "YES"
    return "YES"
