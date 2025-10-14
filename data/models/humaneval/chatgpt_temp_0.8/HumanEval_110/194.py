def exchange(lst1, lst2):
    # Check if lst1 already contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Find all odd elements in lst1
    odd_nums = [num for num in lst1 if num % 2 != 0]
    
    # Try to find even elements in lst2 to swap with odd elements in lst1
    for num in lst2:
        if num % 2 == 0 and len(odd_nums) > 0:
            odd_nums.pop()
    
    # If all odd elements in lst1 were swapped with even elements from lst2, return "YES"
    if len(odd_nums) == 0:
        return "YES"
    else:
        return "NO"
