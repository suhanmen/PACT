def exchange(lst1, lst2):
    # Check if lst1 already contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Find all odd numbers in lst1 and their corresponding even numbers in lst2
    odd_nums = [num for num in lst1 if num % 2 == 1]
    even_nums = [num for num in lst2 if num % 2 == 0 and num not in lst1]
    
    # If there aren't enough even numbers in lst2 to replace all odd numbers in lst1, return "NO"
    if len(odd_nums) > len(even_nums):
        return "NO"
    
    # Replace all odd numbers in lst1 with even numbers from lst2
    for i in range(len(lst1)):
        if lst1[i] in odd_nums:
            lst1[i] = even_nums.pop()
    
    # Check if lst1 contains only even numbers after replacement
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    else:
        return "NO"
