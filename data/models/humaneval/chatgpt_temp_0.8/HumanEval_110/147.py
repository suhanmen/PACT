def exchange(lst1, lst2):
    # Check if lst1 already has all even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Find all odd numbers in lst1
    odd_nums = [num for num in lst1 if num % 2 != 0]
    
    # Find all even numbers in lst2
    even_nums = [num for num in lst2 if num % 2 == 0]
    
    # Check if there are enough even numbers in lst2 to replace the odd numbers in lst1
    if len(even_nums) >= len(odd_nums):
        return "YES"
    
    return "NO"
