def exchange(lst1, lst2):
    # Check if lst1 already contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    even_nums = [num for num in lst1 if num % 2 == 0]  # Get all the even numbers from lst1
    odd_nums = [num for num in lst2 if num % 2 != 0]   # Get all the odd numbers from lst2
    
    # If there are not enough even numbers in lst1 to replace all the odd numbers in lst2, return "NO"
    if len(even_nums) < len(odd_nums):
        return "NO"
    
    # Otherwise, return "YES"
    return "YES"
