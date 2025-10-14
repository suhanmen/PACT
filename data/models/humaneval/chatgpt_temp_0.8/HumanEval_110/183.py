def exchange(lst1, lst2):
    # Check if lst1 already has only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Find the odd numbers in lst1 and even numbers in lst2
    odd_nums = [num for num in lst1 if num % 2 != 0]
    even_nums = [num for num in lst2 if num % 2 == 0]
    
    # If there are not enough even numbers in lst2 to replace all the odd numbers in lst1
    if len(even_nums) < len(odd_nums):
        return "NO"
    
    # Replace odd numbers in lst1 with even numbers in lst2
    for i in range(len(odd_nums)):
        lst1[lst1.index(odd_nums[i])] = even_nums[i]
    
    # Check if lst1 now has only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    else:
        return "NO"
