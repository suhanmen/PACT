def exchange(lst1, lst2):
    # Count the number of odd elements in lst1
    count_odd = len([num for num in lst1 if num % 2 != 0])
    
    # If lst1 already contains only even numbers, return "YES"
    if count_odd == 0:
        return "YES"
    
    # Count the number of even elements in lst2
    count_even = len([num for num in lst2 if num % 2 == 0])
    
    # If there are no even elements in lst2, return "NO"
    if count_even == 0:
        return "NO"
    
    # If there are enough even elements in lst2 to replace all odd elements in lst1, return "YES"
    if count_even >= count_odd:
        return "YES"
    
    # Otherwise, return "NO"
    return "NO"
